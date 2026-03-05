"""
BetterSelf -- AWS Infrastructure Diagram
Shows VPC layout, security groups, and network architecture.

Usage:
    pip install diagrams
    python aws_infrastructure.py
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Aurora, Dynamodb
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.network import APIGateway, VPC, NATGateway, InternetGateway
from diagrams.aws.security import Cognito, SecretsManager, WAF
from diagrams.aws.storage import S3


with Diagram(
    "BetterSelf - AWS Infrastructure",
    show=False,
    direction="TB",
    filename="betterself_aws_infrastructure",
    outformat="png",
):

    waf = WAF("WAF\n(Rate Limiting)")

    with Cluster("VPC (10.0.0.0/16)"):

        igw = InternetGateway("Internet\nGateway")

        with Cluster("Public Subnets (10.0.1.0/24, 10.0.2.0/24)"):
            nat = NATGateway("NAT Gateway")
            api_gw = APIGateway("API Gateway\n(HTTP API)")

        with Cluster("Private Subnets (10.0.3.0/24, 10.0.4.0/24)"):

            with Cluster("Lambda Security Group"):
                lambda_fn = Lambda("FastAPI Lambda\n(Python 3.12)")

            with Cluster("Database Security Group"):
                aurora = Aurora("Aurora Serverless v2\nPostgreSQL 15\n(0.5-4 ACU)")

    cognito = Cognito("Cognito User Pool\n(Email + Apple + Google)")
    dynamodb = Dynamodb("DynamoDB\n(On-Demand, PITR)")
    s3 = S3("S3 Buckets\n(Audio Temp + Assets)")
    secrets = SecretsManager("Secrets Manager\n(DB Credentials)")
    sns = SNS("SNS\n(APNs Platform App)")
    eventbridge = Eventbridge("EventBridge\n(Briefing Cron)")

    waf >> api_gw
    igw >> nat
    api_gw >> Edge(label="Cognito\nAuthorizer") >> cognito
    api_gw >> lambda_fn

    lambda_fn >> Edge(label="Port 5432") >> aurora
    lambda_fn >> Edge(label="VPC Endpoint") >> dynamodb
    lambda_fn >> s3
    lambda_fn >> secrets
    lambda_fn >> sns
    eventbridge >> lambda_fn
