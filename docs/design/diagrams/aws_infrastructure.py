"""
BetterSelf -- AWS VPC & Network Architecture Diagram
Shows VPC layout, security groups, subnets, and network flow.

Usage:
    pip install diagrams
    python aws_infrastructure.py
"""

import os
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway, VPC, PublicSubnet, PrivateSubnet, NATGateway, InternetGateway, Route53
from diagrams.aws.security import Cognito, WAF, SecretsManager
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch

script_dir = os.path.dirname(os.path.abspath(__file__))

graph_attr = {
    "fontsize": "28",
    "bgcolor": "white",
    "pad": "0.8",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "splines": "ortho",
    "dpi": "150",
}

with Diagram(
    "BetterSelf - VPC & Network Architecture",
    filename=os.path.join(script_dir, "aws_vpc_architecture"),
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="png",
):
    internet = Route53("Internet\nTraffic")

    with Cluster("VPC - 10.0.0.0/16", graph_attr={"style": "rounded", "bgcolor": "#E8F4FD"}):
        igw = InternetGateway("Internet\nGateway")

        with Cluster("Edge Protection", graph_attr={"style": "rounded", "bgcolor": "#FFEBEE"}):
            waf = WAF("Web Application\nFirewall (WAF)\nRate Limiting")

        with Cluster("Public Subnets", graph_attr={"style": "rounded", "bgcolor": "#D4EDDA"}):
            pub_a = PublicSubnet("Public A\n10.0.1.0/24\nus-east-1a")
            pub_b = PublicSubnet("Public B\n10.0.2.0/24\nus-east-1b")
            api_gw = APIGateway("API Gateway\n(HTTP API)\nCognito Authorizer")
            nat = NATGateway("NAT\nGateway")

        with Cluster("Private Subnets", graph_attr={"style": "rounded", "bgcolor": "#FFF3CD"}):
            priv_a = PrivateSubnet("Private A\n10.0.3.0/24\nus-east-1a")
            priv_b = PrivateSubnet("Private B\n10.0.4.0/24\nus-east-1b")

            with Cluster("Lambda Security Group\n(Outbound: 443 to Internet + DynamoDB VPC Endpoint)", graph_attr={"style": "dashed", "bgcolor": "#FFF9C4", "pencolor": "#F57F17"}):
                lambda_fn = Lambda("FastAPI Lambda\n(Python 3.12)\n256 MB / 30s timeout")

    with Cluster("VPC Endpoints (Gateway)", graph_attr={"style": "rounded", "bgcolor": "#F3E5F5"}):
        dynamodb = Dynamodb("DynamoDB\n(VPC Endpoint)\nCalendar + Tasks + Habits\n+ Users + Sessions\n+ Conversations")

    with Cluster("Regional Services", graph_attr={"style": "rounded", "bgcolor": "#E8F0FE"}):
        cognito = Cognito("Cognito\nUser Pool")
        s3 = S3("S3 Buckets")
        secrets = SecretsManager("Secrets\nManager")
        logs = Cloudwatch("CloudWatch\nLogs")

    internet >> igw
    igw >> waf
    waf >> api_gw
    api_gw >> Edge(label="JWT\nValidation") >> cognito
    api_gw >> Edge(label="Invoke") >> lambda_fn
    lambda_fn >> Edge(label="VPC Endpoint", color="orange") >> dynamodb
    lambda_fn >> Edge(label="HTTPS", style="dashed", color="gray") >> s3
    lambda_fn >> Edge(label="DB Creds", style="dashed", color="gray") >> secrets
    lambda_fn >> Edge(label="Logs", style="dashed", color="gray") >> logs
    nat >> Edge(label="Outbound\nInternet\n(Bedrock, Transcribe,\nPolly, SNS)") >> igw
