
 <div align="center">

<img width="300px" src="https://github.com/user-attachments/assets/33d90d25-fe2f-4411-aa58-9e971deacb6e" />

<br>


<h2>삼성 청년 SW 아카데미 11기 특화 Safety Car B209</h2>

<p>
    CCTV를 통해 심정지 환자를 인지하고
    AED 키트를 배달해주는 로봇 <strong>Safety Car🚑</strong>
</p>

<br/>
<br/>

</div>

<div>
 
## **목차**

1. 프로젝트 개요 📚
2. 주요 기능 🛠️
3. 기대 효과 🌟
4. 설계 🏗️
5. 기술 스택 🛠️
6. 서비스 시연 
7. 팀원 소개 👥

</div>

<br/>

<div>

## 💫 프로젝트 개요

심정지 환자를 살리는 AED는 1년에 30번도 사용하지 않는 문제점이 있었습니다.

하지만, 실제로 10명 중 7명은 자동심장충격기 설치여부와 위치를 모르기 때문이라는 조사 결과가 있었습니다.

이에 보행자들을 모니터링하며 AED 키트를 직접 배달해줄 수 있다면 심정지 환자들에게 도움이 되리라 생각하여 Safety Car를 기획하게 되었습니다.

<br/>

<h2> 개발 기간📅</h2>

| 개발기간 | 2024.08.19 ~ 2024.10.11 (8주) |
| -------- | ----------------------------- |

</div>

</div>

<br/>
<br/>

<!-- 기술 스택 -->

## 📌 주요 기능

| **기능**                        | **설명**                                                                                                                                           | **사용 기술**                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **실시간 보행자 모니터링**          | - 캠을 통해 실시간 보행자를 모니터링<br>                                     | - UDP를 통한 실시간 스트리밍<br>- Yolo pose 모델을 통한 객체 트래킹                                                                |
| **로봇 2D Map** | - 실시간 로봇 좌표 동기화<br>                                                                     | - 시뮬레이터에서 받아온 맵 정보와 로봇 좌표를 numpy 배열을 통해 2D map 생성                                                                                             |
| **로봇 출동**                    | - 보행자의 쓰러짐이 감지되면, 해당 좌표가 시뮬레이터로 전송, AED 키트 배달이 시작                                                                                                     | - MORAI 시뮬레이터와 서버 간 통신을 통해 전달된 좌표로 출발                                                |
| **로봇 강제 출동**        | - 사용자가 화면을 클릭하면 로봇이 강제 출동<br>                                                                                    | - 사용자가 화면을 클릭하면 해당 좌표로 로봇이 강제 출동 Homography와 이미지 스티칭 기술을 결합한 3D->2D 좌표 변환                                                                                         |
| **로봇 강제 복귀**               | - 사용자가 복귀 명령을 입력하면, 초기 장소로 로봇 강제 복귀<br>                               | - 시뮬레이터에 설정된 초기 좌표값으로 로봇이 복귀 |
| **맵 등록**             | - 바닥 모서리 검출<br>                                                                        | - 두 개의 공간 사진, 바닥의 세로 길이와 가로 길이를 입력받아 모서리를 검출            |
| **맵 등록**          | - 이미지 회전/반전                                                              | - 두 개의 이미지를 하나의 맵처럼 보기 위해 회전하여 바닥을 맞춰줌. openCV의 Image Stretching 사용                                                                                      |
| **맵 등록**          | - 타일 매칭                                                              | - 두 개의 이미지를 하나의 맵처럼 보기 위해 매칭점을 찾아서 선택함. openCV의 Image Stitching 사용                                                                                     |
| **문자 알림**          | - 보행자가 쓰러지면 문자로 쓰러짐 문자를 전송                                                              | - CoolSMS를 통해 문자 알림 서비스 구현                                                                                     |
| **터틀봇 자율주행**          | - 터틀봇의 현재 위치와 목표 좌표까지 global path와 local path 생성<br> - path tracking 알고리즘을 통해 자율주행<br> - Lidar data를 통해 충돌 시 후진 기능                                                              | - A* 알고리즘을 통한 local path 생성<br> - follow the carrot 알고리즘을 활용한 path tracking 구현                                                                                     |
| **Localization과 Mapping**          | - Lidar data와 회전 변환을 활용하여 map 데이터 생성<br> - 비선형 데이터를 임의로 생성하여 로봇의 Odometry 발행 및 구독                                                              | - openCV를 활용한 grid map 구현<br> - particle filter로 비선형 data 구현<br> - SLAM                                                                                     |
| **좌표 데이터 송수신**          | - 터틀봇의 현재 좌표 송신<br> - goal pose data 수신                                                              | - socket.io를 활용한 실시간 데이터 송수신                                                                                     |

<br/>

## 🏗️ 설계
![image (3)](https://github.com/user-attachments/assets/61552a56-e48a-410b-99a7-e976705e3718)


<div align=center><h1>📚 STACKS</h1></div>

<div align=center> 
  <!--frontend-->
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 
    
  <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black"> 
  <img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white">
  <img src="https://img.shields.io/badge/socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white">
  <br>
  
  <!--backend-->
  <img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white"> 
  <img src="https://img.shields.io/badge/c++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  
  <img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white"> 
  <img src="https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  
  <img src="https://img.shields.io/badge/redis-FF4438?style=for-the-badge&logo=redis&logoColor=white">
  <br>
  <!--ROS-->
  <img src="https://img.shields.io/badge/ros-22314E?style=for-the-badge&logo=ros&logoColor=white">
  <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/yolo v8-5C3EE8?style=for-the-badge&logo=&logoColor=white">

  <!--infra-->
  <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> 
  <img src="https://img.shields.io/badge/jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white"> 

  <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=black"> 
  <img src="https://img.shields.io/badge/amazon aws-232F3E?style=for-the-badge&logo=Amazon Web Services&logoColor=white"> 
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <br>
  
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <br>
</div>

## 👥 팀원 소개

<table>
<tr>
    <td align="center"><a href="https://github.com/shanaid"><b>👑박예본</b></a></td>
    <td align="center"><a href="https://github.com/poow810"><b>박하운</b></a></td>
    <td align="center"><a href="https://github.com/boeunyoon"><b>임 권</b></a></td>
    <td align="center"><a href="https://github.com/Geunbeom"><b>서근범</b></a></td>
    <td align="center"><a href="https://github.com/ssuinh"><b>홍수인</b></a></td>
    <td align="center"><a href="https://github.com/"><b>황용주</b></a></td>
  </tr>
 <tr>
     <td align="center"><a href="https://github.com/shanaid"><img src="https://avatars.githubusercontent.com/shanaid" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/poow810"><img src="https://avatars.githubusercontent.com/poow810" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/Al17OTON"><img src="https://avatars.githubusercontent.com/Al17OTON" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/Geunbeom"><img src="https://avatars.githubusercontent.com/Geunbeom" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/ssuinh"><img src="https://avatars.githubusercontent.com/ssuinh" width="130px;" alt=""></a></td>
    <td align="center"><a href="https://github.com/"><img src="https://avatars.githubusercontent.com/" width="130px;" alt=""></a></td>

  </tr>
  <tr>
    <td align="center"><b>BE & 좌표 추출</b></a></td>
    <td align="center"><b>BE & 영상</b></a></td>
    <td align="center"><b>BE & INFRA</b></a></td>
    <td align="center"><b>ROS & SIMULATOR</b></a></td>
    <td align="center"><b>FE & 영상</b></a></td>
    <td align="center"><b>ROS & SIMULATOR</b></a></td>
  </tr>
</table>

<br/>

## 🎞서비스 시연
![아무거나-min (1)](https://github.com/user-attachments/assets/b07ff352-dc21-439e-87ca-9c0d08e51016)







