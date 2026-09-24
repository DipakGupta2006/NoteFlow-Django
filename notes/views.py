from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from django.contrib import messages
from .forms import NoteForm


@login_required(login_url="/accounts/login/")
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "note created sucessfully")
            return redirect("notes:note_list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form":form,  "action": "Create"})

@login_required(login_url="/accounts/login/")
def note_list(request):
    notes = Note.objects.filter(user = request.user, is_archived = False)
    return render(request, "notes/note_list.html", {"notes": notes})


@login_required(login_url="/accounts/login/")
def note_detail(request, pk):
    note = get_object_or_404(Note, pk = pk, user = request.user)
    return render(request, "notes/note_detail.html", { "note": note })

@login_required(login_url="/accounts/login/")
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user = request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, "note updtaed sucessfully")
            return redirect("notes:note_detail", pk = note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {"form":form, "action": "Edit"})

@login_required(login_url="/accounts/login/")
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        messages.success(request, "note deleted sucessfully")
        return redirect("notes:note_list")
    return render(request, 'notes/note_confirm_delete.html', {'note': note})


@login_required(login_url="/accounts/login/")
def note_archive(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.is_archived = True
    note.save()
    return redirect('notes:note_list')


@login_required
def note_archive_list(request):
    archived_notes = Note.objects.filter(user=request.user, is_archived=True)
    return render(request, 'notes/note_archive_list.html', {'notes': archived_notes})

@login_required
def note_unarchive(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.is_archived = False
    note.save()
    return redirect('notes:note_archive_list')