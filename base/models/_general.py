from django.db import models


class WorkoutGif(models.Model):
    """store workouts' gifs and creation date"""
    gif = models.FileField(upload_to="gifs/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WorkoutGif Object: {self.id}"


class ExerciseStatusChoices(models.TextChoices):
    """
    choices for different status.
    exp: ExerciseStatusChoices.DONE.value -> 'done'
    exp: ExerciseStatusChoices.DONE.label -> 'Done'
    exp: ExerciseStatusChoices.DONE.name-> 'DONE'
    """
    CREATED = "created", "Created"
    DOING = "doing", "Doing"
    DONE = "done", "Done"


class ExerciseTypeChoices(models.TextChoices):
    """choices about what is the type of exercise"""
    PUSH_UP = "push_up", "Push Up"
    PULL_UP = "pull_up", "Pull Up"
    PLANK = "plank", "Plank"
    SQUAT = "squat", "Squat"
    CRUNCH = "crunch", "Crunch"


class Exercise(models.Model):
    """stores exercise which is done by the user"""
    title = models.CharField(max_length=50)
    token = models.UUIDField()
    type = models.CharField(max_length=10, choices=ExerciseTypeChoices.choices)
    status = models.CharField(
        max_length=10,
        choices=ExerciseStatusChoices.choices,
        default=ExerciseStatusChoices.CREATED.value
    )
    # numeric fields
    repeat = models.PositiveSmallIntegerField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="exercise_images/", blank=True, null=True)

    # relations
    profile = models.ForeignKey("base.Profile", on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return f"Exercise Object: {self.id} - {self.get_status_display()} - {self.get_type_display()}"


class Client(models.Model):
    """what client says"""
    # text-related fields
    name = models.CharField(max_length=50)
    opinion = models.TextField()

    # image fields
    image = models.ImageField(upload_to="client_avatar/")

    def __str__(self):
        return f"Client Object: {self.id} - {self.name}"
