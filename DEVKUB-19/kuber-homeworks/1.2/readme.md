# Домашнее задание к занятию «Базовые объекты K8S»

### Цель задания

В тестовой среде для работы с Kubernetes, установленной в предыдущем ДЗ, необходимо развернуть Pod с приложением и подключиться к нему со своего локального компьютера. 

------

### Чеклист готовности к домашнему заданию

1. Установленное k8s-решение (например, MicroK8S).
2. Установленный локальный kubectl.
3. Редактор YAML-файлов с подключенным Git-репозиторием.

------

### Инструменты и дополнительные материалы, которые пригодятся для выполнения задания

1. Описание [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) и примеры манифестов.
2. Описание [Service](https://kubernetes.io/docs/concepts/services-networking/service/).

------

### Задание 1. Создать Pod с именем hello-world

1. Создать манифест (yaml-конфигурацию) Pod.
2. Использовать image - gcr.io/kubernetes-e2e-test-images/echoserver:2.2.
3. Подключиться локально к Pod с помощью `kubectl port-forward` и вывести значение (curl или в браузере).


### Ответ на задание 1.

`gcr.io/kubernetes-e2e-test-images/echoserver:2.2` не работает на маке, использовал `gcr.io/kubernetes-e2e-test-images/echoserver-arm:2.2`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-world
  labels:
    app: echoserver
spec:
  containers:
  - name: echoserver-arm-container
    image: gcr.io/kubernetes-e2e-test-images/echoserver-arm:2.2
    ports:
    - containerPort: 8080
```
<img width="1088" alt="image" src="https://github.com/t0hab/devops-19/assets/103331839/2e45e51d-1d46-4cf0-8bfa-53913faef72d">
<img width="1437" alt="image" src="https://github.com/t0hab/devops-19/assets/103331839/ec02efb8-2999-41ee-8c73-3c2794505460">


------

### Задание 2. Создать Service и подключить его к Pod

1. Создать Pod с именем netology-web.
2. Использовать image — gcr.io/kubernetes-e2e-test-images/echoserver:2.2.
3. Создать Service с именем netology-svc и подключить к netology-web.
4. Подключиться локально к Service с помощью `kubectl port-forward` и вывести значение (curl или в браузере).

### Ответ на задание 2.

Pod netology-web
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: netology-web
  labels:
    app: netology-web
spec:
  containers:
  - name: echoserver-arm-container
    image: gcr.io/kubernetes-e2e-test-images/echoserver:2.2
    ports:
    - containerPort: 8080
```

Service netology-svc
```yaml
apiVersion: v1
kind: Service
metadata:
  name: netology-svc
spec:
  selector:
    app: netology-web
  ports:
  - name: http
    port: 80
    targetPort: 8080
  type: NodePort
  ```
  <img width="1087" alt="image" src="https://github.com/t0hab/devops-19/assets/103331839/7004ee53-b3d7-4d31-af6a-f5495e5ea562">



------

