import mlflow

def calculate(x,y):
    return(x/y)


if __name__ == '__main__':
    x= 100
    y= 200
    with mlflow.start_run():
        result = calculate(x,y)
        print(result)
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_param("result",result)


