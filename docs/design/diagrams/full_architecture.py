"""
BetterSelf -- Full Architecture Diagram
Generates a PNG diagram of the complete system architecture.

Usage:
    pip install diagrams
    python full_architecture.py
"""

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Aurora, Dynamodb
from diagrams.aws.integration import SNS, Eventbridge
from diagrams.aws.ml import Transcribe
from diagrams.aws.network import APIGateway, VPC
from diagrams.aws.security import Cognito
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.generic.device import Mobile


with Diagram(
    "BetterSelf - System Architecture",
    show=False,
    direction="TB",
    filename="betterself_architecture",
    outformat="png",
):

    ios_app = Mobile("iOS App\n(Swift + SwiftUI)")

    with Cluster("AWS Cloud"):

        cognito = Cognito("Cognito\nUser Pool")
        api_gw = APIGateway("API Gateway\n(HTTP API)")

        with Cluster("VPC"):

            with Cluster("Private Subnets"):
                lambda_fn = Lambda("Lambda\n(FastAPI + Mangum)")

            with Cluster("Database Layer"):
                dynamodb = Dynamodb("DynamoDB\n(Users, Sessions,\nConversations)")
                aurora = Aurora("Aurora Serverless v2\n(Calendar, Tasks,\nHabits, Analytics)")

        with Cluster("AI & Voice Services"):
            bedrock = Lambda("Bedrock\n(Claude LLM)")
            transcribe = Transcribe("Transcribe\n(Speech-to-Text)")
            polly = Lambda("Polly\n(Text-to-Speech)")

        s3 = S3("S3\n(Audio Temp Storage)")
        sns = SNS("SNS\n(Push Notifications)")
        eventbridge = Eventbridge("EventBridge\n(Scheduled Tasks)")
        pinpoint = Lambda("Pinpoint\n(Analytics)")

    ios_app >> Edge(label="Auth") >> cognito
    ios_app >> Edge(label="REST API") >> api_gw
    api_gw >> Edge(label="JWT Auth") >> cognito
    api_gw >> lambda_fn

    lambda_fn >> dynamodb
    lambda_fn >> aurora
    lambda_fn >> bedrock
    lambda_fn >> transcribe
    lambda_fn >> polly
    lambda_fn >> s3
    lambda_fn >> sns

    sns >> Edge(label="APNs Push") >> ios_app
    eventbridge >> Edge(label="Daily Briefing\nCron") >> lambda_fn
    pinpoint >> Edge(label="Analytics") >> ios_app
