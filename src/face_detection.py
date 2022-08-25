import face_recognition
import cv2
import numpy as np
import pickle as pk

class Face:

    def __init__(self, path = ""):
        self._path = path
        # self.face_encoding = face_encoding

    def _convert_into_face_encoding(self):
        try:
            new_image = face_recognition.load_image_file(self._path)
            new_face_encoding = face_recognition.face_encodings(new_image)[0]
            return new_face_encoding
        except:
            return None

    def return_face_encoding(self):
        try:
            encoding = self._convert_into_face_encoding()
            return pk.dumps(encoding)
        except:
            return None

class CompareFace(Face):
    def compare_faces(self, path, face_encodings):
        acknowledge = {'index': -1}
        try:
            self._path = path
            face_encoding = self._convert_into_face_encoding()
            face_encodings = list(map(pk.loads, face_encodings))
            matches = face_recognition.compare_faces(face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                acknowledge['index'] = best_match_index
                acknowledge['confidence'] = 95
            
        except:
            pass
        
        return acknowledge
        '''
        known_encoding = pk.loads(obj)
        name = False
        available = {name: -1}
        for face_encoding in known_encoding:
            matches = face_recognition.compare_faces(face_encoding, unknown)
            face_distances = face_recognition.face_distance(known_encoding, unknown)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = True
                available = {name: best_match_index}

        return available
        '''

