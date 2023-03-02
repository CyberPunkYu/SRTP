from fastapi import FastAPI, File, UploadFile
import uvicorn, os, uuid
from fastapi.responses import JSONResponse
# 声明fastapi的实例
app = FastAPI(title="基于transformer的自动图像标注", version="2.4.0", description="程序总入口")

# 测试
@app.get("/test/")
async def root():
    return {"message": "TRANSFORMER"}


@app.post("/uploadfile/")
async def uploadfile(image: UploadFile = File(...)):
    # 创建文件夹
    try:
        if not os.path.exists("getImages"):
            os.makedirs("getImages")
    except Exception as e:
        print(e)
    # 获得文件名
    suffix_arr = image.filename.split(".")
    suffix = suffix_arr[len(suffix_arr) - 1]
    file_name = os.getcwd() + "/getImages/" + str(uuid.uuid1()) + "." + suffix
    # 将图片保存到本地
    with open(file_name, "wb+") as f:
        f.write(image.file.read())
        f.close()
    # 将图片地址返回
    return JSONResponse(
        content = {
            "filename": file_name
            }
        )

@app.get("/getlabel/")
async def getlabel(image: UploadFile = File(...)):
    # 创建文件夹
    try:
        if not os.path.exists("getImages"):
            os.makedirs("getImages")
    except Exception as e:
        print(e)
    # 获得文件名
    suffix_arr = image.filename.split(".")
    suffix = suffix_arr[len(suffix_arr) - 1]
    file_name = os.getcwd() + "/getImages/" + str(uuid.uuid1()) + "." + suffix
    # 将图片保存到本地
    with open(file_name, "wb+") as f:
        f.write(image.file.read())
        f.close()
    # 将图片地址返回
    return {
            "filename": file_name
           }


if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='127.0.0.1',
                port=8000,
                reload=True)