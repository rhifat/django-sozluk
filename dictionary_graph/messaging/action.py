from django.core.validators import ValidationError
from django.urls import reverse_lazy
from django.utils import timezone

from graphene import ID, List, Mutation, String

from dictionary.models import Author, Conversation, ConversationArchive, Message
from dictionary.utils.validators import validate_user_text

from ..utils import login_required


class DeleteConversation(Mutation):
    class Arguments:
        mode = String()
        pk_set = List(ID)

    redirect = String()

    @staticmethod
    @login_required
    def mutate(_root, info, mode, pk_set):
        if mode not in ("archived", "present"):
            raise ValueError("the requested mode is not valid")

        if mode == "present":
            model = Conversation
            url_name = "messages"
        else:
            model = ConversationArchive
            url_name = "messages-archive"

        model.objects.filter(holder=info.context.user, pk__in=pk_set).delete()
        return DeleteConversation(redirect=reverse_lazy(url_name))


class ArchiveConversation(Mutation):
    class Arguments:
        pk_set = List(ID)

    redirect = String()

    @staticmethod
    @login_required
    def mutate(_root, info, pk_set):
        for conversation in Conversation.objects.filter(holder=info.context.user, pk__in=pk_set):
            conversation.messages.filter(recipient=info.context.user, read_at__isnull=True).update(
                read_at=timezone.now()
            )
            conversation.archive()

        return ArchiveConversation(redirect=reverse_lazy("messages-archive"))


class ComposeMessage(Mutation):
    class Arguments:
        body = String()
        recipient = String()

    feedback = String()

    @staticmethod
    @login_required
    def mutate(_root, info, body, recipient):
        sender = info.context.user
        if len(body) < 3:
            return ComposeMessage(feedback="az bir şeyler yaz yeğenim")

        try:
            recipient_ = Author.objects.get(username=recipient)
            validate_user_text(body)
        except Author.DoesNotExist:
            return ComposeMessage(feedback="böyle biri yok yalnız")
        except ValidationError as error:
            return ComposeMessage(feedback=error.message)

        sent = Message.objects.compose(sender, recipient_, body)

        if not sent:
            return ComposeMessage(feedback="mesajınızı gönderemedik ne yazık ki")

        return ComposeMessage(feedback="mesajınız sağ salim gönderildi")