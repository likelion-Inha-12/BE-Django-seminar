from django.db import models

class Part(models.Model):
    name = # 파트명(FE/BE/ALL)

class Assignment(models.Model):
    title = # 과제 제목
    content = # 과제 내용
    part = # part 모델과의 연관관계 매핑
    github_link = # 과제의 깃허브 링크
    created_at = # 과제 생성일
    expire_at = # 과제 마감일

class Submission(models.Model):
    content = # 제출물 내용
    github_link = # 제출물의 깃허브 링크
    assignment = # Assignment 모델과의 연관관계 매핑