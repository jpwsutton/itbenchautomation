# IT Bench Automation

Welcome to the IT Bench Agent Automation Repository!

## Onboarding

To onboard your agent and get started benchmarking, please follow the following steps:

1. Create an empty repository (or use a repository of your choice) on GitHub:
    - The repository must be set to private.
    - The onboarding process will create a file called `agent_manifest.json` at the root of the repository, so if using an existing repository make sure that there will not be a clash.
2. Install the [`ibm-itbench`](https://github.com/apps/ibm-itbench) app into the repository that you created in step 1.
3. Fill out and submit [this issue template](https://github.com/jpwsutton/itbenchautomation/issues/new?template=onboarding.yaml) with the details of the agent you are developing and provide the URL to the GitHub Repo you created in step 1 e.g. https://github.com/jpwsutton/my-test-agent
4. Once the registration issue has been approved, an automated process will generate a manifest for your agent to access the IT Bench Server and will save it to the root of your repository from step 1. You can now download this file and use it with the agent harness to initiate a benchmark. 
