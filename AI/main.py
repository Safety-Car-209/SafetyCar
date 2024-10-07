from fastapi import FastAPI
import httpx

app = FastAPI()

SPRING_BOOT_URL = 'https://j11b209.p.ssafy.io/pyapi'


async def send_coordinate(x, y, camera_id):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{SPRING_BOOT_URL}/transform_point/",
                data={
                    "x": x,
                    "y": y,
                    "camera_id": camera_id
                },
                timeout=10.0  # 요청 타임아웃 설정
            )
            print(response)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
            
            
        except httpx.HTTPError as e:
            print(f"HTTP 오류: {e}")
            return {"status": "error", "message": str(e)}
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return {"status": "error", "message": str(e)}

    try:
        response_data = response.json()
        if 'x_floor' in response_data and 'y_floor' in response_data:
            return {
                "status": "success",
                "x_floor": response_data["x_floor"],
                "y_floor": response_data["y_floor"]
            }
        else:
            return {"status": "error", "response": response_data}
    except ValueError:
        print("JSON 파싱 오류:", response.content)
        return {"status": "error", "response": response.content}