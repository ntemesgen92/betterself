# Milestone 12: Lambda & API Gateway

## Status
Not Started

## Goal
Set up FastAPI project structure with Mangum adapter for Lambda, deployment pipeline, and health check endpoints. Establishes the serverless API layer connecting API Gateway to Lambda.

## Dependencies
Milestones 9 (CDK Foundation), 10 (Auth Infrastructure)

## Plan
- Create FastAPI project with Mangum adapter
- Deploy Lambda function via CDK with VPC attachment
- Configure API Gateway routes to Lambda
- Implement health check endpoint with DB connectivity verification
- Set up structured logging and request tracing
- Create deployment pipeline with GitHub Actions

## Key Files
| File | Description |
|------|-------------|
| api/main.py | FastAPI app entry point |
| api/requirements.txt | Python dependencies |
| infrastructure/stacks/api_stack.py | Lambda function, API Gateway configuration |
| api/routers/__init__.py | Router module initialization |
| Dockerfile | Lambda container deployment |

## Implementation Details
1. **FastAPI project**: Create in api/ directory
2. **Mangum adapter**: Install and configure (FastAPI → Lambda handler)
3. **Lambda function**: Python 3.12 runtime, 256MB memory (tune later), 30s timeout, VPC-attached (private subnet), environment variables for DB connections
4. **API Gateway**: Configure routes to Lambda
5. **Health check**: GET /health endpoint that verifies DB connectivity
6. **Logging**: Structured logging with AWS Lambda Powertools
7. **Request ID**: Middleware for tracing
8. **Dockerfile**: Lambda container deployment for larger dependencies
9. **GitHub Actions**: Build, test, deploy on push to main

## Testing
- Lambda deploys successfully
- /health returns 200
- API Gateway routes to Lambda correctly
- Logs appear in CloudWatch
- Cold start time is acceptable (<3s)

## Notes
- **Duration**: 2 days
