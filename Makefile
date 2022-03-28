install:
	helm package helm && helm install minanode helm-0.1.0.tgz

uninstall:
	helm uninstall minanode