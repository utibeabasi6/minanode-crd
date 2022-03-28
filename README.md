# MinaNode CRD

## Prerequisites
To follow along with this guide, you need to have the following installed

If you are running this with Docker compose, you need to install the following:
- Docker
- Docker compose

If you are deploying to LKE(Linode Kubernetes Engine), you need to have the following setup:
- Linode cli
- Terraform
- A linode account
- Kubectl
- helm

If you are deploying to a local kubernetes cluster, you need to have the following setup:
- Kubectl
- Minikube
- helm

## How to run
- Run the command `kubectl apply -f manifests/minanodedefinition.yaml` to create the custom resource definition in the cluster
- Run the command make install to package the helm chart and deploy the example node

