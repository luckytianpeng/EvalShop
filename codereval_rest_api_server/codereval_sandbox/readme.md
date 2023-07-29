
```shell
sudo docker build --tag codereval_sandbox .
```

```shell
sudo docker rm -f $(sudo docker ps -a -q)
```

```shell
sudo docker image prune -a
```

```shell
sudo docker image prune
```
