import ensurepip
from gettext import install
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.aws.integration import SQS
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
    price=input("What is the retail price of a solar panel?").lower()
    country=input("Enter Country").lower()
#    fit=input("Does " + country + " have a feed-in-tariff? (Y/N)").lower()
  

    if country=="italy":
        fit=input("Does " + country + " have a feed-in-tariff? (Y/N)").lower()
        if fit=="y":
            amount=int(input("Feed-in-tariff amount: "))
            percentage=int(input("Feed-in-tariff percentage received by producer: "))
            if percentage==100:
                with Diagram("System Diagram", show=True, direction="TB"):
                    government = ELB("Government")
                    producer = RDS ("Producer")
                    customer = S3("Customer")
                    ELB >> RDS << S3
            else:
                disposal=input("Does the producer manage the recycling themselves? (Y/N)").lower()
                recyclecost=int(input("How much does it cost to recycle?"))
                #totalcost=(amount*(percentage/100))-recyclecost
                consortiumamount= amount-(amount*(percentage/100))
                totalcost=amount-recyclecost
            
                if disposal=="y":
                    display=input("Do you want to display the material or money flow?").lower()
                    while display!="clear":

                        with Diagram("System Diagram", show=True, direction="TB"):
                            producer = RDS ("Producer")
                            government = ELB("Government")
                            consortium = EC2("Consortium")
                            customer = S3("Customer")
                            recycler = SQS("Recycler")

                        
                            if display == "money":
                                print("Display money")

                                government \
                                >> Edge(label="£" + str(amount*(percentage/100))) \
                                >> producer \
                                
                                government \
                                >> Edge(label="£" + str(amount-(amount*(percentage/100)))) \
                                >> consortium \

                                customer \
                                >> Edge(label="£" + str(price)) \
                                >> producer \

                                producer \
                                >> Edge(label="£" + str(recyclecost)) \
                                >> recycler \

                                consortium \
                                >> Edge(label="£" + str(amount-(amount*(percentage/100)))) \
                                >> producer \
                                
                                if(totalcost < 0):
                                    print("The producer makes a loss of £{0}.".format(str(abs(totalcost))))
                                
                                else:
                                    print("The producer keeps £{0} profit from the feed-in-tariff.".format(str(abs(totalcost))))
        
                            elif display == "material":

                                producer \
                                >> Edge(label="Delivery") \
                                >> customer \

                                recycler \
                                >> Edge(label="Collection") \
                                >> customer \
                            
                            elif display == "both":

                                government \
                                >> Edge(label="FIT payment") \
                                >> producer \
                                
                                government \
                                >> Edge(label="FIT percentage") \
                                >> consortium \

                                producer \
                                >> Edge(label="Delivery") \
                                >> customer \

                                customer \
                                >> Edge(label="Payment") \
                                >> producer \

                                recycler \
                                >> Edge(label="Collection") \
                                >> customer \
                                
                                producer \
                                >> Edge(label="Payment") \
                                >> recycler \

                                consortium \
                                >> Edge(label="FIT amount") \
                                >> producer \
                            
                        display=input("Do you want to display the material or money flow?").lower()

                elif disposal=="n":

                    #recyclecost=int(input("How much does it cost to recycle?"))
                    #totalcost=amount-recyclecost

                    with Diagram("System Diagram", show=True, direction="TB"):
                        producer = RDS ("Producer")
                        government = ELB("Government")
                        consortium = EC2("Consortium")
                        customer = S3("Customer")
                        recycler = SQS("Recycler")

                        government \
                        >> Edge(label="£" + str(amount*(percentage/100))) \
                        >> producer \
                        
                        government \
                        >> Edge(label="£" + str(amount-(amount*(percentage/100)))) \
                        >> consortium \

                        producer \
                        >> Edge(label="Delivery") \
                        >> customer \

                        customer \
                        >> Edge(label="Payment") \
                        >> producer \

                        customer \
                        >> Edge(label="Collection") \
                        >> recycler \

                        consortium \
                        >> Edge(label="£" + str(recyclecost)) \
                        >> recycler

                        if(totalcost < 0):
                            print("The producer must pay the consortium £{0}".format(totalcost))
                            producer \
                            >> Edge(label="£" + str(abs(totalcost))) \
                            >> consortium
                        
                        else:
                            print("The producer receives £{0} from the consortium".format((amount-(amount*(percentage/100)))-recyclecost))
                            
                            consortium \
                            >> Edge(label="£" + str(((amount-(amount*(percentage/100)))-recyclecost))) \
                            >> producer
                

        elif fit=="n":
            with Diagram("System Diagram", show=True, direction="TB"):
                RDS("Producer")

    else:
        print('invalid')
