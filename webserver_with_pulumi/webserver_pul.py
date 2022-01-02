# diagram.py
from diagrams import Cluster, Diagram, Node , Edge
from diagrams.custom import Custom
from diagrams.aws.compute import EC2 , SAR, LocalZones
from diagrams.aws.general import GenericFirewall, InternetAlt2 ,User

# This determines the whole diagram is shaped as how its big or small
dia_graph_attr = {
    "fontsize": "25",
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
    "pencolor":"orange",
    "fontcolor":"black",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}
sec_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"red",
    "fontcolor":"red",
    "fontname":"Helvetica bold",
    "fontsize":"10.0"
}


with Diagram("\nWebserver Using Pulumi", show=False, graph_attr=dia_graph_attr) as diag:
    with Cluster(f"{' '*10}AWS Cloud", graph_attr=AWS_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="4,6" )
        Node(label="", shape="plaintext", pin="true", pos="4,6" )
        aws_cloud = SAR(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.35,8.2")        

    with Cluster(f"{' '*12}ap-south-1", graph_attr=region_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="3,6.3" )
        Node(label="", shape="plaintext", pin="true", pos="3.5,7" )        
        region = LocalZones(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.5", height="0.5", 
            pin="true", pos="-0.15,7.65")
        cont1 = EC2("t2.micro", pin="true", pos="2,6.6.2",
                     width="1.2", height="1.2")
    
    with Cluster(f"{' '*8}Security Group", graph_attr=sec_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="1.8,6.5" )
        Node(label="", shape="plaintext", pin="true", pos="2.2,6.5" )        
        security_group = GenericFirewall(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="0.3", height="0.3", color = "red",
            pin="true", pos="1.3,7.59")

    User_view = User(pin="true",fixedsize="true",pos="-2.2,6.59",
                    width="1", height="1")

    User_view >> Edge(style="bold",label=f"port 80{' '* 10}", color="black") >> cont1