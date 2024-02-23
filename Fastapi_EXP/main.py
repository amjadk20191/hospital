import mysql.connector

cnx = mysql.connector.connect(user='root', password='amjad2001',
                              host='localhost', database='hospital')
from fastapi import FastAPI, Request, HTTPException, Depends
from experta import *
from fastapi.security import OAuth2PasswordBearer
import jwt

from fastapi.middleware.cors import CORSMiddleware
from jwt import decode as jwt_decode


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

final=False


respons = dict()

class DiagnosisSystem(KnowledgeEngine):


    @Rule(Fact(dis=None))
    def data(self):
        respons['question']="حدد المشكلة او موقع الالم"
        respons['answer']=['العين','الجلد','نسائية','بولية','انف-اذن-حنجرة','صدرية','البطن']
        respons['name']='dis'
        # ans = ans.strip()
        # self.declare(Fact(dis=ans))

    @Rule(Fact(dis='العين'))
    def f0(self):
        global final

        #print("توجه لطبيب عينية  ")
        respons['finalanswer'] ="توجه لطبيب عينية"
        final = True

    @Rule(Fact(dis='الجلد'))
    def f1(self):
        global final

        # print("توجه لطبيب جلدية ")
        respons['finalanswer'] ="توجه لطبيب جلدية "
        final = True


    @Rule(Fact(dis='نسائية'))
    def f2(self):
        # ans = input("هل يترافق مع اعراض نسائية؟ ")

        respons['question'] = "هل يترافق مع اعراض نسائية؟ "
        respons['answer'] = ['لا', 'نعم']
        respons['name'] = 'statuse'
        # ans = ans.strip ()
        # self.declare(Fact(statuse=ans))
    @Rule(Fact(statuse='نعم'))
    def f4(self):
        global final

        # print("توجهي لطبيب نسائية ")
        respons['finalanswer'] ="توجهي لطبيب نسائية "
        final = True



    @Rule(Fact(statuse='لا'))
    def f5(self):
        global final

        # print("توجهي لطبيب بولية ")
        respons['finalanswer'] = "توجهي لطبيب بولية "
        final = True


    @Rule(Fact(dis='بولية'))
    def f6(self):
        # ans = input("ذكر أم انثى ؟")
        # ans = ans.strip()
        # self.declare(Fact(gender=ans))
        respons['question'] = "ذكر أم انثى ؟"
        respons['answer'] = ['ذكر', 'أنثى']
        respons['name'] = 'gender'


    @Rule(Fact(gender='ذكر'))
    def f7(self):
        print("////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        global final

        # print("توجه لطبيب بولية ")
        respons['finalanswer'] = "توجهي لطبيب بولية "
        final = True


    @Rule(Fact(gender='أنثى'))
    def f8(self):
        # ans = input("هل يترافق مع أعراض نسائية ؟")
        # ans = ans.strip()
        # self.declare(Fact(semptoms=ans))
        respons['question'] = "هل يترافق مع أعراض نسائية"
        respons['answer'] = ['يترافق مع اعراض', 'لا يترافق مع اعراض']
        respons['name'] = 'semptoms'


    @Rule(Fact(semptoms='يترافق مع اعراض'))
    def f8_1(self):
        global final

        # print("توجهي لطبيب نسائية")
        respons['finalanswer'] = "توجهي لطبيب نسائية"
        final = True

    @Rule(Fact(semptoms='لا يترافق مع اعراض'))
    def f8_2(self):
        global final

        # print("توجهي لطبيب بولية")
        respons['finalanswer'] = "توجهي لطبيب بولية "
        final = True


    @Rule(Fact(dis='انف-اذن-حنجرة'))
    def f9(self):
        global final

        # print("توجه لطبيب انف - اذن - حنجرة ")
        respons['finalanswer'] = "توجهي لطبيب بولية "
        final = True


    @Rule(Fact(dis='صدرية'))
    def f10(self):
        respons['question'] = "هل يوجد الم بالصدر ؟"
        respons['answer'] = ['لا يوجد الم', 'يوجد الم']
        respons['name'] = 'pain'


        # ans = input("هل يوجد الم بالصدر ؟")
        # ans = ans.strip ()
        # self.declare(Fact(pain=ans))

    @Rule(Fact(pain='لا يوجد الم'))
    def f11(self):
        global final

        # print("توجه لطبيب صدرية ")
        respons['finalanswer'] = "توجه لطبيب صدرية "
        final = True


    @Rule(Fact(pain='يوجد الم'))
    def f12(self):
        # ans = input("هل يميل نحو العنق والذراع اليسرى ؟")
        # ans = ans.strip()
        # self.declare(Fact(location=ans))
        respons['question'] = "هل يميل نحو العنق والذراع اليسرى ؟"
        respons['answer'] = ['يميل نحو العنق والذراع اليسرى','لا يميل نحو العنق والذراع اليسرى']
        respons['name'] = 'location'


    @Rule(Fact(location='يميل نحو العنق والذراع اليسرى'))
    def f13(self):
        global final

        # print("توجه لطبيب قلبية")
        respons['finalanswer'] ="توجه لطبيب قلبية"
        final = True


    @Rule(Fact(location='لا يميل نحو العنق والذراع اليسرى'))
    def f14(self):
        global final

        # print("توجه لطبيب صدرية")
        respons['finalanswer'] ="توجه لطبيب صدرية"
        final = True


    @Rule(Fact(dis='البطن'))
    def f15(self):
        # ans = input("هل يترافق مع غثيان او اقياء ؟ ")
        # ans = ans.strip()
        # self.declare(Fact(vomit=ans))
        respons['question'] = "هل يترافق مع غثيان او اقياء ؟ "
        respons['answer'] = ['يترافق مع غثيان او اقياء', 'لا يترافق مع غثيان او اقياء']
        respons['name'] = 'vomit'


    @Rule(Fact(vomit='يترافق مع غثيان او اقياء'))
    def f16(self):
        global final

        # print("توجهي لطبيب هضمية")
        respons['finalanswer'] = "توجهي لطبيب هضمية"
        final = True


    @Rule(Fact(vomit='لا يترافق مع غثيان او اقياء'))
    def f17(self):
        # ansr = input("هل يترافق مع عسر تبول ؟ ")
        # ansr = ansr.strip()
        # self.declare(Fact(pee=ansr))
        respons['question'] = "هل يترافق مع عسر تبول ؟ "
        respons['answer'] = ['يترافق مع عسر تبول', 'لا يترافق مع عسر تبول']
        respons['name'] = 'pee'


    @Rule(Fact(pee='يترافق مع عسر تبول'))
    def f18(self):
        global final

        # print("توجه لطبيب هضمية")
        respons['finalanswer'] = "توجهي لطبيب هضمية"
        final = True




    @Rule(Fact(pee='لا يترافق مع عسر تبول'))
    def f19(self):
        # ansr = input("هل توجد اعراض قلبية ؟ ")
        # ansr = ansr.strip()
        # self.declare(Fact(heart=ansr))
        respons['question'] = "هل توجد اعراض قلبية ؟ "
        respons['answer'] = ['توجد اعراض قلبية', 'لا توجد اعراض قلبية']
        respons['name'] = 'heart'


    @Rule(Fact(heart='توجد اعراض قلبية'))
    def f20(self):
        global final

        # print("توجه لطبيب قلبية")
        respons['finalanswer'] = "توجه لطبيب قلبية"
        final = True


    @Rule(Fact(heart='لا توجد اعراض قلبية'))
    def f21(self):
        # ansr = input("هل توجد اعراض تنفسية ؟ ")
        # ansr = ansr.strip()
        # self.declare(Fact(breath=ansr))
        respons['question'] = "هل توجد اعراض تنفسية ؟ "
        respons['answer'] = ['يترافق مع اعراض تنفسية','لا يترافق مع اعراض تنفسية']
        respons['name'] = 'breath'


    @Rule(Fact(breath='يترافق مع اعراض تنفسية'))
    def f22(self):
        global final

        # print("توجه لطبيب صدرية")
        respons['finalanswer'] ="توجه لطبيب صدرية"
        final = True



    @Rule(Fact(breath='لا يترافق مع اعراض تنفسية'))
    def f23(self):
        global final

        # print("توجه لطبيب هضمية")
        respons['finalanswer'] ="توجه لطبيب هضمية"
        final = True
























JWT_SECRET_KEY = 'django-insecure-*nqld+2!$l^a5t$%r94!$ej$yme4t_3*nu%==xz%8g_!lh@n8('


def get_payload( jwt_token):
        payload = jwt_decode(
            jwt_token,JWT_SECRET_KEY, algorithms=["HS256"])

        return payload
def get_user_credentials( payload):
        """
        method to get user credentials from jwt token payload.
        defaults to user id.
        """
        user_id = payload['user_id']
        return user_id

def get_id(jwt_token):

    jwt_payload = get_payload(jwt_token.split()[1])

    user_credentials = get_user_credentials(jwt_payload)
    return user_credentials


@app.post("/")
async def get_tables(request: Request):


    user_id = get_id(request.headers.get('Authorization'))
    cursor = cnx.cursor()
    query = f"SELECT id FROM patient_patient WHERE user_id={user_id}"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    print(result[0][0])

    json_body = await request.json()
    # comment = json_body.get("comment")




    global final,respons
    respons = dict()


    Patient_id=result[0][0]
    if 'name' in json_body:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")



        cursor = cnx.cursor()
        update_query = f"UPDATE patient_exp SET {json_body.get('name')}='{json_body.get('value')}'  WHERE Patient_id={Patient_id}"
        cursor.execute(update_query)
        cnx.commit()
        cursor.close()







    cursor = cnx.cursor()
    query = f"SELECT Patient_id, dis, statuse, gender, semptoms, pain, location, vomit, pee, heart, breath FROM patient_exp WHERE Patient_id={Patient_id}"

    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    engine = DiagnosisSystem()
    engine.reset()
    # engine.declare(Fact(dis=result[0][1]))

    print(result[0])
    print(result[0][1])
    print(result[0][1] == None)
    print(type(result[0]))
    print(result[0].index(None))
    index = 0
    for i in range(1, len(result[0])):
        if not result[0][i] is None:
            print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
            print(result[0][i])
            index = i




    fact=["dis", "statuse", "gender", "semptoms", "pain", "location", "vomit", "pee", "heart", "breath"]

    if index==0:
        engine.declare(Fact(dis=result[0][1]))
    else:
        print(fact[index-1])
        print(result[0][index])

        exec(f"engine.declare(Fact({fact[index-1]}='{result[0][index]}'))")
    engine.run()

    if final :
        cursor = cnx.cursor()
        update_query = f"UPDATE patient_exp SET dis=null, statuse=null , gender=null, semptoms=null, pain=null, location=null, vomit=null, pee=null, heart=null, breath=null WHERE Patient_id={Patient_id}"
        cursor.execute(update_query)
        cnx.commit()
        cursor.close()
        final=False




    return respons