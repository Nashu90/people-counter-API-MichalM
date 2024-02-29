from flask import Flask
from flask_restful import Resource, Api
from flask import request
import cv2
import numpy as np # zadanie
from urllib.request import urlopen # zadanie

app = Flask(__name__)
api = Api(app)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

#class HelloWorld2(Resource):
#    def get(self, id):
#        return {'hello': id}

class PeopleCounter(Resource):
    def get(self):
        img = cv2.imread('foto.jpg')
        boxes, weights = hog.detectMultiScale(img, winStride=(8, 8))
        return {'count': len(boxes)}

class PeopleCounterURL(Resource): # dodane
    def get(self):
        url = request.args.get('url')
        print(url)
        req = urlopen(url)
        image = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(image, -1)
        boxes, weights = hog.detectMultiScale(img, winStride=(8, 8))
        return {'count': len(boxes)}

class PeopleCounterURLPro(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        img_name = request.args.get('img')
        img = cv2.imread(img_name)
        boxes, weights = hog.detectMultiScale(img, winStride=(8, 8))
        return {'count': len(boxes)}

#api.add_resource(Nowe, '/nowe') # dodane
#api.add_resource(Nowe2, '/nowe2') # dodane
#api.add_resource(HelloWorld,'/hello')
#api.add_resource(HelloWorld2,'/hello2/<string:id>')

api.add_resource(PeopleCounter, '/zadanie1')
api.add_resource(PeopleCounterURL, '/zadanie2')
api.add_resource(PeopleCounterURLPro, '/zadanie3')

if __name__ == '__main__':
    app.run(debug=True)


#class INCORRECT(Resource):
 #   def get(self):
 #       url = request.args.get('url')
 #       print(url)
 #       img = cv2.imread(url)
 #       boxes, weights = hog.detectMultiScale(img, winStride=(8, 8))
 #       return {'count': len(boxes)}