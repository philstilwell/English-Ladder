"""A natural counter exchange, including the handoff to the drink bar."""
from books.leadership_pilot import dialogue


def revise(book):
    u = book['units'][0]
    u['cast'] = [('Nia', 'Counter barista'), ('Alex', 'Customer'), ('Sam', 'Bar barista')]
    u.update(dialogue('''
Alex|Could I get a regular latte to go? Just the one, please.
Nia|Of course. By [[regular::Regular is ambiguous here: Alex means non-decaf, while the cafe uses it for the middle size.]], do you mean our middle size, or coffee that isn't decaf?
Alex|Not decaf. A small cup would be plenty. Sorry, I couldn't see the sizes from the back of the queue.
Nia|No problem. A [[small::Small is the size Alex chooses; it does not change the separate coffee choice.]] latte. Would you like it hot or iced?
Alex|Hot, please. Just the usual coffee in it, with no extra shot.
Nia|Small, hot, [[non-decaf::Non-decaf identifies the requested coffee, not an exact caffeine quantity.]]. What would you like for milk?
Alex|What does it normally come with? I couldn't read that part of the menu either.
Nia|Our standard is [[dairy milk::Dairy milk is the stated default for this cafe, and Alex accepts it.]]. Is that all right?
Alex|Yes, that's fine. And no vanilla or anything sweet, please.
Nia|I'll mark [[no syrup::This explicitly records the omission Alex requests instead of assuming it.]]. You're taking it with you, right?
Alex|Yes, thanks. I did say that at the start, but it's quite noisy here.
Nia|You did. I've got [[takeaway::Takeaway preserves the service choice Alex gave at the start.]] on the ticket. Sam, this one isn't ready to make yet; I'm just checking the details.
Sam|Thanks. I haven't started it. I can see small on the ticket now; I heard regular earlier.
Nia|Yes, Alex meant the coffee, not our [[middle size::Middle size is the cafe's meaning of regular, not the size Alex ordered.]]. The order is for a small.
Alex|That's right. And still hot, please. I only changed what I called the size.
Sam|Still [[hot::Hot is the confirmed temperature style; clarifying size did not change it.]]. I'll wait for Nia to finish checking the ticket before I make it.
Alex|Could you run through the whole thing once more? I don't want to hold everyone up with a remake.
Nia|Here's the [[read-back::A read-back combines the separate choices so Alex can check the complete order.]]: one small hot latte, non-decaf, standard dairy milk, no syrup, to go.
Alex|Exactly that. Thanks for checking instead of just giving me the middle cup.
Nia|Great, the [[ticket::The ticket records the confirmed request; it does not mean the drink has already been prepared.]] matches. Sam, you can use that order now. Alex, I'll take your payment here.
'''))
    u['setting'] = 'Alex uses regular to mean non-decaf; this cafe uses it for a size. Nia confirms the order before handing it to Sam at the bar.'
