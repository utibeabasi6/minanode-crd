import kopf
from kubernetes import client, config
import yaml
from os import path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def gen_template(inputfile, variables, output):
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template(inputfile)
    print("Generating template".center(80, "-"))
    with open(f"manifests/{output}", "w") as f:
        f.write(template.render(variables=variables))

@kopf.on.create('minanodes')
def create_fn(body, **kwargs):
    k8s_apps_v1 = client.AppsV1Api()
    # gen_template("configmap.yaml.j2", {"producer": body["spec"]["producer"], "mina_priv_key": body["spec"]["privKeyPass"]}, "configmap.yaml")
    gen_template("mina-node.yaml.j2", {"name": body["spec"]["name"], "producer": body["spec"]["producer"], "mina_priv_key": body["spec"]["privKeyPass"]}, "mina-node.yaml")

    with open("manifests/mina-node.yaml") as f:
        mn = yaml.safe_load(f)
        kopf.adopt(mn)
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=mn, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)


