import ensurepip
from gettext import install
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

while True:
    country=input("Enter Country").lower()
#    fit=input("Does " + country + " have a feed-in-tariff? (Y/N)").lower()
  

    if country=="italy":
        fit=input("Does " + country + " have a feed-in-tariff? (Y/N)").lower()
        if fit=="y":
            percentage=int(input("Feed-in-tariff percengage received by producer: "))
            if percentage==100:
                with Diagram("System Diagram", show=True, direction="TB"):
                    ELB("Government") >> RDS("Producer")
            else:
                with Diagram("System Diagram", show=True, direction="TB"):
                    ELB("Government") >> [RDS("Producer"),
                                EC2("Consortium")]

        elif fit=="n":
            with Diagram("System Diagram", show=True, direction="TB"):
                RDS("Producer")

    else:
        print('invalid')

#'"ELB("Producer") >> [EC2("worker1"),
#            EC2("worker2"),
#            EC2("worker3"),
#            EC2("worker4"),
#            EC2("worker5")] >> RDS("events")

  # if country=="italy":
    #     with Diagram("System Diagram", show=True, direction="TB"):
    #         RDS("Producer")
    #         if fit=="y":
    #             with Diagram("System Diagram", show=True, direction="TB"):
    #                 ELB("Government") >> RDS("Producer")