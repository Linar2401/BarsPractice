from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from account.models import CustomUser
from task_manager.models import *


class TeamCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse('account:login')
    model = Team
    fields = ['name', 'managers', 'workers', 'board']
    template_name = 'task_manager/create_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class BoardCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse('account:login')
    model = Board
    fields = ['name', 'room']
    template_name = 'task_manager/create_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class ProcessCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse('account:login')
    model = Process
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/create_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = reverse('account:login')
    model = Task
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/create_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse('account:login')
    model = Team
    fields = ['name', 'managers', 'workers', 'board']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class BoardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse('account:login')
    model = Board
    fields = ['name', 'room']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class ProcessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse('account:login')
    model = Process
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse('account:login')
    model = Task
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse('account:login')
    model = Team
    fields = ['name', 'managers', 'workers', 'board']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class BoardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse('account:login')
    model = Board
    fields = ['name', 'room']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class ProcessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse('account:login')
    model = Process
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse('account:login')
    model = Task
    fields = ['name', 'board', 'status']
    template_name = 'task_manager/update_form.html'

    def test_func(self):
        return self.request.user.position.isManager()