

#urllib
#requests

import requests
class HTTP:
    def get(self,url,return_json=True):
        r=requests.get(url)
        #restful
        # json or txt
        if r.status_code!=200:
            return {} if return_json else r.text
        return r.json() if return_json else r.text
        # if r.status_code==200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''