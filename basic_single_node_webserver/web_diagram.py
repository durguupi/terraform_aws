# diagram.py
from diagrams import Cluster, Diagram, Node , Edge
from diagrams.aws.compute import EC2 , SAR
from diagrams.aws.general import InternetAlt2

# This determines the whole image is shaped as how its big or small
graph_attr = {
    "fontsize": "35",
    # "bgcolor": "lightgray",
    "layout" : "neato",
    "margin" : "0.8,0.4",
    
}

# This attributes are for the cluster where we are defining AWS cloud
AWS_graph_attr = {
    "style":"solid",
    "bgcolor":"transparent",
    "pencolor":"orange",
    "penwidth":"4.0",
    "fontcolor":"orange",
    "fontname":"Helvetica bold",
    "fontsize":"22.0",
    "labelloc":"t",
    "labeljust":"l",
}
# This attributes are for the cluster where we are defining region
region_graph_attr = {
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "pencolor":"orange",
    "fontcolor":"black",
    "fontname":"Sans-Serif",
    "fontsize":"18.0"
}
# This attributes are for the cluster where we are defining internet
internet_graph_attr = {
    "fontcolor":"black",
    "style":"rounded,dotted",
    "bgcolor":"transparent",
    "labeljust":"c",
    "fontname":"Helvetica bold",
    "fontsize":"13.0",
    "penwidth":"0.0"
}

# Giving the diagram name 
with Diagram("\n\nSimple Web Server", show=False, graph_attr=graph_attr):

    with Cluster(f"\n{' '*20}AWS Cloud", graph_attr=AWS_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="0,0" )
        Node(label="", shape="plaintext", pin="true", pos="4,4" )
        aws_cloud = SAR(
            label="", fontsize="6", loc="t",
            fixedsize="true", width="1.2", height="1.2", 
            pin="true", pos="-0.35,5")        
   
    with Cluster(f"{' '*5}ap-south-1\n\n", graph_attr=region_graph_attr):
        Node(label="", shape="plaintext", pin="true", pos="1,1" )
        Node(label="", shape="plaintext", pin="true", pos="3,3" )        
        ec2_clus = EC2("t2.micro\n",
                        fontsize="20", 
                        pin="true", 
                        pos="2,2", )

    with Cluster(f"\n{' '*8}INTERNET", graph_attr=internet_graph_attr):

        internet = InternetAlt2(pin="true",fixedsize="true")
        
    internet >> Edge(style="bold",label="port 80") >> ec2_clus

