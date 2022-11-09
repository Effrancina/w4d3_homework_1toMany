from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import author_repository, book_repository
from models.book import Book