# Milestone 9: AWS CDK Foundation

## Status
Not Started

## Goal
Set up the base AWS CDK project with VPC, subnets, security groups, and foundational stacks for the BetterSelf backend. This provides the networking and security foundation upon which all other infrastructure will be built.

## Dependencies
None (can be done in parallel with iOS work)

## Plan
- Initialize CDK project with Python
- Create VPC stack with public and private subnets across 2 AZs
- Configure security groups for Lambda
- Add CDK context for environment configuration
- Set up CDK Nag for security validation
- Create GitHub Actions workflow for CDK deployment pipeline

## Key Files
| File | Description |
|------|-------------|
| infrastructure/app.py | CDK app entry point, stack assembly |
| infrastructure/stacks/vpc_stack.py | VPC, subnets, NAT gateway, security groups |
| infrastructure/requirements.txt | Python dependencies for CDK |
| infrastructure/cdk.json | CDK configuration and context |

## Implementation Details
1. **Initialize CDK project**: Run `cdk init app --language python` to scaffold the project structure
2. **VPC stack**: Create VPC with 2 AZs, public and private subnets, NAT gateway (or VPC endpoints for cost savings)
3. **Security groups**: Lambda SG (outbound to internet + DynamoDB via VPC endpoint)
4. **CDK context**: Configure dev/staging/prod environments via cdk.json context
5. **CDK Nag**: Add CDK Nag for security best practices validation
6. **CI/CD**: Set up GitHub Actions workflow for `cdk diff` on PR and `cdk deploy` on merge to main

## Testing
- `cdk synth` produces valid CloudFormation
- `cdk deploy` creates VPC successfully
- Security groups have correct rules

## Notes
- **Duration**: 2 days
- Consider VPC endpoints instead of NAT gateway for cost savings in development
