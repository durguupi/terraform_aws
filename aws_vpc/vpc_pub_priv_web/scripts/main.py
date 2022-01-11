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
    "margin" : "-1.7,-1.7",
}
AWS_graph_attr = {
    "style":"solid",
    "bgcolor":"transparent",
    "pencolor":"orange",
    "penwidth":"4.0",
    "fontcolor":"orange",
    "fontname":"Helvetica bold",
    "fontsize":"15.0",
    "labelloc":"t",
    "labeljust":"l",
}

# This attributes are for the cluster where we are defining region
region_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"red",
    "fontcolor":"red",
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

public_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"forestgreen",
    "fontcolor":"forestgreen",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}

private_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"dodgerblue",
    "fontcolor":"dodgerblue",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}


with Diagram("\nVPC with Pubic webserver and Private instance", show=False, graph_attr=dia_graph_attr) as diag:
    with Cluster(f"{' '*10}AWS Cloud", graph_attr=AWS_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0,4" )
        Node(label="", shape="plaintext", pin="true", pos="7,8" )
        aws_cloud = SAR(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.45,9")        

    with Cluster(f"{' '*12}ap-south-1", graph_attr=region_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.5,4.3" )
        Node(label="", shape="plaintext", pin="true", pos="6.8,7.6" )        
        region = LocalZones(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.14,8.5")

    with Cluster(f"VPC\n\n{' '*35}10.0.0.0/16", graph_attr=vpc_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0.8,4.5" )
        Node(label="", shape="plaintext", pin="true", pos="6.5,7.7" )        
        vpc = VPC(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="0.36,8.2")

            
    with Cluster(f"{' '*8}Public Subnet{' '*15}ap-south-1a\n\n\n{' '*8}10.0.1.0/24", graph_attr=public_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="1.3,5" )
        Node(label="", shape="plaintext", pin="true", pos="2.8,7" )        
        public_subnet = PublicSubnet(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="0.7,7.6", )
        routepub = RouteTable(
            label=f"{' '*6}PublicRouteTable\n\n\n\n", fontsize="8", loc="t",
            fixedsize="true", width="0.4", height="0.4", fontcolor="forestgreen",
            pin="true", pos="0.7,7")
        web1 = EC2("t2.micro", pin="true", pos="2.1,6",fontsize="8",
                     width="1", height="1")
        

    with Cluster(f"{' '*8}Private Subnet{' '*15}ap-south-1b\n\n\n{' '*4}10.0.2.0/24", graph_attr=private_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="4.5,5" )
        Node(label="", shape="plaintext", pin="true", pos="6,7" )        
        private_subnet = PrivateSubnet(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.3", height="0.3",
            pin="true", pos="3.85,7.6")
        routepub = RouteTable(
            label=f"{' '*6}PrivateRouteTable\n\n\n\n", fontsize="8", loc="t",
            fixedsize="true", width="0.4", height="0.4", fontcolor="dodgerblue",
            pin="true", pos="6.5,7")
        web2 = EC2("t2.micro", pin="true", pos="5.2,6",fontsize="8",
                     width="1", height="1")


    with Cluster("\n\n\nIGW", graph_attr=vpc_graph_attr):
        igw = InternetGateway(label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="0.16,6")


    User_view = User(pin="true",fixedsize="true",pos="-2.2,6",
                    width="1", height="1")

    User_view >> Edge(style="solid",label=f"port 80", color="black") >> \
            igw >> Edge(style="solid",label=f"", color="black") >> web1

    web1 >> Edge(style="striped",label=f"SSH 22{' '* 16}", color="forestgreen", fontsize="10",
              fontcolor="forestgreen") >> web2

    web1 << Edge(style="dotted",label=f"\nPING", color="dodgerblue",fontcolor="dodgerblue",
                        fontsize="10" ) >> web2