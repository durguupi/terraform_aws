# diagram.py
from diagrams import Cluster, Diagram, Node , Edge
from diagrams.custom import Custom
from diagrams.aws.compute import EC2 , SAR, LocalZones
from diagrams.aws.general import GenericFirewall, InternetAlt2 ,User
from diagrams.aws.network import *


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
# This attributes are for the cluster where we are defining Private Subnet
private_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"dodgerblue",
    "fontcolor":"dodgerblue",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}

# This determines the outline of diagram 
with Diagram("\nVPC with Public and Private Subnet in each AZ using count", show=False, graph_attr=dia_graph_attr) as diag:
    with Cluster(f"{' '*10}AWS Cloud", graph_attr=AWS_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0,4" )
        Node(label="", shape="plaintext", pin="true", pos="10,8" )
        # This is used for displaying the AWS cloud ICON
        aws_cloud = SAR(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-1.45,9")        

# This determines the outline used for the Region 
    with Cluster(f"{' '*12}Region{' '*2}ap-south-1", graph_attr=region_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.2,4.4" )
        Node(label="", shape="plaintext", pin="true", pos="9.6,7.8" )   
    # This is used for dispalying the Region icon     
        region = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-1.14,8.5")

# This determines the outline used for the VPC
    with Cluster(f"{' '*12}VPC{' '*100}10.0.0.0/16", graph_attr=vpc_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.3,4.7" )
        Node(label="", shape="plaintext", pin="true", pos="9.2,7.6" ) 
        # This is used for dispalying the VPC icon       
        vpc = VPC(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.8,8")

# This determines the outline used for the ============Avalilabity Zone -1 ====================
    with Cluster(f"{' '*5}AZ1{' '*5}ap-south-1a", graph_attr=az_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.3,5" )
        Node(label="", shape="plaintext", pin="true", pos="2,7.2" )        
        az1 = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3", 
            pin="true", pos="-0.3,7.8")

# This determines the outline used for the Public Subnet in AZ1
    with Cluster(f"{' '*8}Public Subnet{' '*8}10.0.0.0/24", graph_attr=public_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.5,6.8" )
        Node(label="", shape="plaintext", pin="true", pos="1.7,6.8" )  
        public_subnet_az1 = PublicSubnet(
            label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="-0.1,7.4", )

# This determines the outline used for the Private Subnet in AZ1
    with Cluster(f"{' '*8}Private Subnet{' '*8}10.0.3.0/24", graph_attr=private_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.5,5.2" )
        Node(label="", shape="plaintext", pin="true", pos="1.7,5.2" )  
        private_subnet_az1 = PrivateSubnet(
            label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="-0.1,5.8", )

# This determines the outline used for the ============Avalilabity Zone 2 ====================
    with Cluster(f"{' '*5}AZ2{' '*5}ap-south-1b", graph_attr=az_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="3.8,5" )
        Node(label="", shape="plaintext", pin="true", pos="5.6,7.2" )        
        az2 = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3", 
            pin="true", pos="3.2,7.8")

# This determines the outline used for the Public Subnet in AZ2
    with Cluster(f"{' '*8}Public Subnet{' '*8}10.0.1.0/24", graph_attr=public_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="4,6.8" )
        Node(label="", shape="plaintext", pin="true", pos="5.4,6.8" )  
        public_subnet_az2 = PublicSubnet(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="3.4,7.4", )

# This determines the outline used for the Private Subnet in AZ2
    with Cluster(f"{' '*8}Private Subnet{' '*8}10.0.4.0/24", graph_attr=private_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="4,5.2" )
        Node(label="", shape="plaintext", pin="true", pos="5.4,5.2" )  
        private_subnet_az2 = PrivateSubnet(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="3.4,5.8", )
    
# This determines the outline used for the ============Avalilabity Zone 3 ====================
    with Cluster(f"{' '*5}AZ3{' '*5}ap-south-1c", graph_attr=az_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="8.8,5" )
        Node(label="", shape="plaintext", pin="true", pos="7.4,7.2" )        
        az3 = LocalZones(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3", 
            pin="true", pos="6.8,7.8")

# This determines the outline used for the Public Subnet in AZ3
    with Cluster(f"{' '*8}Public Subnet{' '*8}10.0.2.0/24", graph_attr=public_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="8.6,6.8" )
        Node(label="", shape="plaintext", pin="true", pos="7.6,6.8" )  
        public_subnet_az3 = PublicSubnet(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="7,7.4", )

# This determines the outline used for the Private Subnet in AZ3
    with Cluster(f"{' '*8}Private Subnet{' '*8}10.0.5.0/24", graph_attr=private_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="8.6,5.2" )
        Node(label="", shape="plaintext", pin="true", pos="7.6,5.2" )  
        private_subnet_az3 = PrivateSubnet(label="", fontsize="6", loc="t",fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="7,5.8", )

# Defining the internet Gateway Attributes    
    with Cluster("\n\n\nIGW", graph_attr=vpc_graph_attr):
        igw = InternetGateway(label="", fontsize="6", loc="t",fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.9,6")

# Defining the Route Table Attributes for Public subnet
    routepub = RouteTable(label=f"{' '*6}PublicRouteTable\n\n\n\n", fontsize="8", loc="t",
            fixedsize="true", width="0.4", height="0.4", fontcolor="forestgreen",pin="true", pos="2.2,8.4")

# Connecting all public subnets to the route Table
    routepub - Edge(style="dotted",label="",color="forestgreen",) - [public_subnet_az1,public_subnet_az2,public_subnet_az3]

# Defining the Route Table Attributes for Private subnet 
    routepriv = RouteTable(
            label=f"{' '*6}PrivateRouteTable\n\n\n\n", fontsize="8", loc="t",
            fixedsize="true", width="0.4", height="0.4", fontcolor="dodgerblue",pin="true", pos="6.6,3.9")

# Connecting all Private subnets to the route Table 
    routepriv - Edge(style="dotted",label="",color="dodgerblue",) - [private_subnet_az1,private_subnet_az2,private_subnet_az3]