import pymysql2
class Pool:
    def __init__(self):
        self.config=pymysql2.infos()
    def create(self):
        return pymysql2.pool(self.config)
    def destroy(self,pool):
        pool.destroy()
