from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=10)

class Assignment(models.Model):
    title = models.CharField(max_length=200)  # 과제 제목
    content = models.TextField()  # 과제 내용
    part = models.ForeignKey(Part, on_delete=models.CASCADE)  # part 모델과의 연관관계 매핑
    github_link = models.URLField()  # 과제의 깃허브 링크
    created_at = models.DateTimeField(auto_now_add=True)  # 과제 생성일
    expire_at = models.DateTimeField()  # 과제 마감일

class Submission(models.Model):
    content = models.TextField()  # 제출물 내용
    github_link = models.URLField()  # 제출물의 깃허브 링크
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)  # Assignment 모델과의 연관관계 매핑
