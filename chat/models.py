from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )

    def __str__(self):
        return self.sender.username + " - " + self.receiver.username


class Message(models.Model):
    conversation = models.ForeignKey(
        "chat.ChatRoom",
        on_delete=models.CASCADE,
        related_name="conversation",
        default=False,
    )
    sender1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender1", default=False
    )
    receiver1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver1", default=False
    )
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ("timestamp",)
