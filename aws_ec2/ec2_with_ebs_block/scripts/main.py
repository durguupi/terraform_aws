# diagram.py
from turtle import shape
from diagrams import Cluster, Diagram, Node , Edge
from diagrams.custom import Custom
from diagrams.aws.compute import EC2 , SAR, LocalZones
from diagrams.aws.general import GenericFirewall, InternetAlt2 ,User
from diagrams.aws.network import *
from diagrams.aws.storage import ElasticBlockStoreEBSVolume, ElasticBlockStoreEBS ,EBS


# This determines the whole diagram is shaped as how its big or small
dia_graph_attr = {
    "fontsize": "26",
    "bgcolor": "azure1",
    "layout" : "neato",
    "fontname":"Helvetica bold",
    "margin" : "-1.5,-1.5",
}
# This attributes are for the cluster where we are defining AWS
AWS_graph_attr = {
    "style":"rounded, solid",
    "bgcolor":"transparent",
    "pencolor":"orange",
    "penwidth":"4.0",
    "fontcolor":"orange",
    "fontname":"Helvetica bold",
    "fontsize":"15.0",
}

# This attributes are for the cluster where we are defining region
region_graph_attr = {
    "style":"rounded,solid",
    "bgcolor":"transparent",
    "pencolor":"orange",
    "penwidth":"2.0",
    "fontcolor":"orange",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}

# This attributes are for the cluster where we are defining region
vpc_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"purple",
    "fontcolor":"purple",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}
# This attributes are for the cluster where we are defining Availablity Zone
az_graph_attr = {
    "style":"rounded,dashed",
    "bgcolor":"transparent",
    "pencolor":"red",
    "fontcolor":"red",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}
# This attributes are for the cluster where we are defining Public Subnet
public_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"forestgreen",
    "fontcolor":"forestgreen",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}


# This determines the outline of diagram 
with Diagram("\nEC2 instance with EBS Volume Attached", show=False, graph_attr=dia_graph_attr) as diag:
    with Cluster(f"{' '*10}AWS Cloud", graph_attr=AWS_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0,4" )
        Node(label="", shape="plaintext", pin="true", pos="4,8" )
        # This is used for displaying the AWS cloud ICON
        aws_cloud = SAR(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-1.6,9")        

# This determines the outline used for the Region 
    with Cluster(f"{' '*12}Region{' '*2}ap-south-1", graph_attr=region_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.1,4.3" )
        Node(label="", shape="plaintext", pin="true", pos="3.7,7.8" )   
    # This is used for dispalying the Region icon     
        region = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.4", height="0.4", 
            pin="true", pos="-1.2,8.6")

# This determines the outline used for the VPC
    with Cluster(f"{' '*12}VPC{' '*10}10.0.0.0/16", graph_attr=vpc_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.1,4.6" )
        Node(label="", shape="plaintext", pin="true", pos="3.4,7.8" ) 
        # This is used for dispalying the VPC icon       
        vpc = VPC(label="", fontsize="6", loc="t",fixedsize="true", width="0.4", height="0.4", 
            pin="true", pos="-0.8,8.3")

# This determines the outline used for the ============Avalilabity Zone -1 ====================
    with Cluster(f"{' '*5}AZ1{' '*5}ap-south-1a", graph_attr=az_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.2,4.8" )
        Node(label="", shape="plaintext", pin="true", pos="3.1,7.4" )        
        az1 = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3", 
            pin="true", pos="-0.6,8")

# This determines the outline used for the Public Subnet in AZ1
    with Cluster(f"{' '*8}Public Subnet{' '*8}10.0.0.0/24", graph_attr=public_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.3,5" )
        Node(label="", shape="plaintext", pin="true", pos="2.8,7.1" )  
        public_subnet_az1 = PublicSubnet(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", 
                                        height="0.3", pin="true", pos="-0.3,7.7", )
        routepub = RouteTable(label=f"{' '*4}PublicRouteTable\n\n\n\n", fontsize="8", loc="t",
            fixedsize="true", width="0.4", height="0.4", fontcolor="forestgreen",
            pin="true", pos="-0.23,7.2")
    with Cluster(f"", graph_attr=region_graph_attr): 
        web1 = EC2("t2.micro", pin="true", pos="0.6,6.2",fontsize="8",
                     width="1", height="1")  
        ebs = EBS("EBS", pin="true", pos="2.6,6.2",fontsize="8",
                     width="1", height="1")

# Defining the internet Gateway Attributes    
    with Cluster("\n\n\nIGW", graph_attr=vpc_graph_attr):
        igw = InternetGateway(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-1.1,6.2")

    
    User_view = User(pin="true",fixedsize="true",pos="-2.8,6.2",
                    width="1", height="1")

    User_view >> Edge(style="dashed",label=f"", color="black",) - \
            igw >> Edge(style="dashed",label=f"Port 80\n\n", color="black") >> web1

    web1 - Edge(style="dotted",label="",color="darkgreen",) << ebs
    