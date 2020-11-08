# Clustered App
1. Run cluster
```shell script
# Default Amount of Copies
sudo docker-compose up --scale app=2 -d --build --force-recreate

# Custom Amount of Copies
sudo docker-compose up --scale app={amount_of_copies} -d --build --force-recreate
```
2. Checkout http://localhost to see result
