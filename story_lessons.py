"""Short, human-readable lesson sources; generated pages are built by editorial.py."""


def vocabulary(*entries):
    return [dict(term=term, part_of_speech=part, definition=definition) for term, part, definition in entries]


def quiz(question, correct, wrong_one, wrong_two, explanation):
    return dict(question=question, options=[correct, wrong_one, wrong_two], correct_option_index=0,
                option_feedback=[explanation, "Try again. " + explanation, "Try again. " + explanation])


def lesson(title, overview, sentences, words, grammar, questions, prediction, discussion):
    return dict(title=title, overview=overview, topic=title, news_brief_sentences=sentences,
                vocabulary=words, grammar=dict(zip(["concept", "explanation", "example_quote"], grammar)),
                quiz=questions, prediction=prediction, discussion=discussion)


STORIES = [
    {
        "slug": "city-trees", "category": "Nature & city life",
        "photo_note": "An urban park illustrates the green space discussed in this lesson.",
        "source": {"name": "US Environmental Protection Agency: trees and city heat", "link": "https://www.epa.gov/heatislands/using-trees-and-vegetation-reduce-heat-islands"},
        "supporting_sources": ["https://www.epa.gov/heatislands/benefits-trees-and-vegetation", "https://www.epa.gov/heatislands/community-member-tree-planting-efforts"],
        "levels": {
            "beginner": lesson(
                "Can trees cool a city?", "Find out why a tree can be more than a pretty part of a street.",
                ["Trees can help cool a city.", "Their leaves give people shade on hot days.", "Trees also release water into the air, and this helps cool it.", "A tree near a building can reduce the need for air conditioning.", "People need to choose trees that suit the local climate.", "Young trees need care after people plant them."],
                vocabulary(("shade", "noun", "a place where something blocks direct sunlight"), ("reduce", "verb", "to make something smaller or less"), ("climate", "noun", "the usual weather in a place over many years")),
                ("Can + verb", "Use can with the basic form of a verb to describe what is possible.", "Trees can help cool a city."),
                [quiz("How can leaves help people on hot days?", "They give shade.", "They make sunlight stronger.", "They stop all wind.", "Leaves give people shade by blocking direct sunlight."),
                 quiz("What do trees release into the air?", "Water", "Air conditioning", "Buildings", "The story says trees release water into the air."),
                 quiz("What does reduce mean?", "Make less", "Make more", "Keep exactly the same", "To reduce something is to make it smaller or less."),
                 quiz("Which tree should people choose?", "One that suits the local climate", "Only the tallest tree", "Any tree, in any place", "The tree needs to suit the local climate."),
                 quiz("Which sentence uses can correctly?", "Trees can help.", "Trees can helps.", "Trees can helping.", "Use the basic verb help after can.")],
                "Look at the photo. Where would you stand on a hot day?",
                ["Describe a place with trees near your home.", "Where could your town use more shade? Explain your choice."]),
            "intermediate": lesson(
                "Can trees cool a city?", "Explore the connection between greener streets and cooler places to live.",
                ["City trees can make their surroundings cooler in more than one way.", "Their branches provide shade, while water released through their leaves helps cool the air.", "When trees shade buildings, they can reduce the demand for air conditioning.", "However, planting any available tree is not enough: the species must suit the local climate.", "Young trees also require regular maintenance after planting.", "A successful planting project therefore involves both choosing suitable trees and caring for them."],
                vocabulary(("surroundings", "plural noun", "the area around a person or thing"), ("demand", "noun", "the amount of something that is needed or wanted"), ("maintenance", "noun", "regular work that keeps something in good condition")),
                ("While to connect ideas", "While can connect two different actions happening in the same situation.", "Their branches provide shade, while water released through their leaves helps cool the air."),
                [quiz("Which two cooling effects are described?", "Shade and water released through leaves", "Wind and artificial lighting", "Rain and stronger sunlight", "The passage describes shade and the cooling effect of water released through leaves."),
                 quiz("Why might a shaded building need less air conditioning?", "The tree helps keep it cooler.", "The tree produces electricity.", "The tree changes its size.", "Trees that shade buildings can reduce demand for air conditioning."),
                 quiz("What does maintenance refer to here?", "Caring for trees after planting", "Measuring buildings once", "Buying a tree without planting it", "Maintenance is the regular care that young trees need."),
                 quiz("What does however introduce?", "A limitation to consider", "An unrelated event", "An exact temperature", "However introduces a qualification: trees must suit the local climate."),
                 quiz("Which conclusion matches the text?", "Tree planting needs planning and follow-up care.", "Every tree suits every city.", "Planting alone guarantees success.", "Both suitable selection and continued care are part of a successful project.")],
                "Would planting more trees always be enough to improve a street?",
                ["Explain two ways trees can cool their surroundings.", "Your neighborhood can plant trees in one place. Where would you choose, and why?"]),
            "advanced": lesson(
                "Can trees cool a city?", "Consider why effective urban planting depends on what happens after the photo opportunity.",
                ["Urban vegetation moderates local temperatures through shade and the release of water into the atmosphere.", "Where tree cover shades buildings, demand for air conditioning can also decline.", "These benefits, however, do not make planting an adequate substitute for long-term stewardship.", "Species selection must reflect the local climate, while newly planted trees require ongoing maintenance.", "A project evaluated solely by the number of trees planted may therefore overlook the conditions needed for those trees to survive.", "Rather than treating planting as a single achievement, communities should consider it the beginning of a sustained commitment."],
                vocabulary(("moderates", "verb", "makes something less extreme"), ("stewardship", "noun", "responsible care and management over time"), ("sustained", "adjective", "continued over a period of time")),
                ("A reduced passive clause", "Evaluated solely by the number of trees planted shortens that is evaluated solely by the number of trees planted. It describes the project without a full relative clause.", "A project evaluated solely by the number of trees planted may therefore overlook the conditions needed for those trees to survive."),
                [quiz("What is the main argument?", "Planting should begin a continuing commitment.", "Urban trees provide no practical benefits.", "Tree counts are the only useful measure.", "The final sentence frames planting as the beginning of a sustained commitment."),
                 quiz("Which outcome is presented as possible rather than guaranteed?", "Reduced demand for air conditioning", "The disappearance of all urban heat", "The survival of every planted tree", "Can also decline expresses a possibility, not a universal guarantee."),
                 quiz("What does stewardship emphasize?", "Responsible care over time", "Publicity at a single event", "A count with no follow-up", "Stewardship means continuing responsible care and management."),
                 quiz("Why might a tree count be an incomplete measure?", "It may overlook what trees need to survive.", "It proves every species is suitable.", "It records all maintenance work.", "The author argues that counting planting alone can overlook survival conditions."),
                 quiz("Which expansion preserves the meaning of a project evaluated solely…?", "A project that is evaluated solely…", "A project that evaluates itself solely…", "A project before it evaluated solely…", "The reduced clause has passive meaning: the project is evaluated.")],
                "What would count as success for a city tree-planting program five years later?",
                ["Defend two measures of success beyond the number of trees planted.", "Summarize the writer's argument, then identify one question the passage leaves unanswered."]),
        },
    },
    {
        "slug": "food-market", "category": "Food & conversation",
        "photo_note": "A real market in Kyiv sets the scene; the conversation below is fictional.",
        "scenario_note": "An original practice scenario. The people and dialogue are fictional; the photograph shows a real market.",
        "levels": {
            "beginner": lesson(
                "A small question. A new conversation.", "Practice asking for what you need on a visit to a food market.",
                ["Mina visits a food market on Saturday.", "She wants to buy tomatoes for dinner.", "She asks a vendor, 'How much are these tomatoes?'", "The vendor says, 'They cost three dollars for one kilo.'", "Mina asks, 'Could I have half a kilo, please?'", "The vendor puts the tomatoes in her bag, and Mina says thank you."],
                vocabulary(("vendor", "noun", "a person who sells things"), ("cost", "verb", "to have a particular price"), ("half", "noun", "one of two equal parts")),
                ("A polite request with could", "Could I have…? is a polite way to ask for something.", "Mina asks, 'Could I have half a kilo, please?'"),
                [quiz("What does Mina want to buy?", "Tomatoes", "Bread", "Apples", "Mina wants tomatoes for dinner."),
                 quiz("Who answers Mina's question?", "A vendor", "A bus driver", "A teacher", "A vendor is the person selling the tomatoes."),
                 quiz("How much does Mina ask for?", "Half a kilo", "Three kilos", "One whole kilo", "Mina asks for half a kilo."),
                 quiz("Which question asks about the price?", "How much are these tomatoes?", "Where is the market?", "What is your name?", "How much…? asks about the price in this conversation."),
                 quiz("Which request is polite?", "Could I have half a kilo, please?", "Give tomatoes now.", "You must give me tomatoes.", "Could I have… please? is a polite request.")],
                "You want to buy something, but you do not know the price. What could you ask?",
                ["Practice the conversation with a partner. Choose a different food.", "What do you like buying at a market? Explain in two sentences."]),
            "intermediate": lesson(
                "A small question. A new conversation.", "Find out how asking one extra question can make a shopping conversation easier.",
                ["Mina stops at a market stall to buy tomatoes for dinner.", "After asking the price, she explains that she only needs enough for two people.", "The vendor suggests half a kilo, but Mina is unsure how much that is.", "Instead of pretending to understand, she asks whether he could show her.", "He places a few tomatoes on the scale so that she can see the quantity.", "Mina thanks him and realizes that a simple request for clarification made the conversation easier."],
                vocabulary(("stall", "noun", "a stand or small space where goods are sold"), ("quantity", "noun", "the amount of something"), ("clarification", "noun", "an explanation that makes something easier to understand")),
                ("So that to explain purpose", "So that introduces the purpose of an action: why someone does it.", "He places a few tomatoes on the scale so that she can see the quantity."),
                [quiz("Why does Mina need help after hearing the suggestion?", "She is unsure what half a kilo looks like.", "She has forgotten what she wants.", "She cannot find the stall.", "Mina is unsure how much half a kilo is."),
                 quiz("What does Mina do instead of pretending?", "She asks the vendor to show her.", "She leaves without speaking.", "She changes the price herself.", "She asks whether he could show her the amount."),
                 quiz("Why does the vendor use the scale?", "To show the quantity", "To choose the color", "To hide the price", "He puts tomatoes on the scale so she can see the quantity."),
                 quiz("What does clarification mean here?", "Making an unclear amount understandable", "Refusing to answer a question", "Agreeing without understanding", "Clarification makes something easier to understand."),
                 quiz("What does so that introduce in the passage?", "The purpose of the vendor's action", "A completely unrelated result", "A past event before the visit", "So that she can see the quantity explains why he uses the scale.")],
                "When you do not understand a suggestion, how can you keep the conversation going?",
                ["Role-play the scene, using a different item and quantity.", "Describe a time when asking one more question helped you understand something."]),
            "advanced": lesson(
                "A small question. A new conversation.", "Explore how a polite request can repair a misunderstanding without disrupting the exchange.",
                ["At a market stall, Mina asks for enough tomatoes to prepare dinner for two.", "The vendor recommends half a kilo, a quantity she finds difficult to visualize.", "Reluctant to agree without understanding, she asks whether he could demonstrate what that amount looks like.", "By placing several tomatoes on the scale, he makes an abstract measurement tangible.", "Her request for clarification allows the exchange to continue without either speaker treating uncertainty as a failure.", "The encounter illustrates how a modest, well-phrased question can support mutual understanding."],
                vocabulary(("visualize", "verb", "form a clear mental picture of something"), ("tangible", "adjective", "concrete and possible to see or experience directly"), ("mutual", "adjective", "shared by both people or sides")),
                ("By + -ing to describe a method", "By followed by an -ing form explains how an action achieves a result.", "By placing several tomatoes on the scale, he makes an abstract measurement tangible."),
                [quiz("What difficulty does Mina encounter?", "She cannot easily picture the suggested quantity.", "She cannot decide which meal to prepare.", "She disputes the vendor's price.", "The quantity is difficult for her to visualize; the passage does not describe a price dispute."),
                 quiz("What makes the measurement tangible?", "Seeing actual tomatoes on the scale", "Hearing the same number louder", "Changing the subject", "The physical demonstration turns an abstract amount into something visible."),
                 quiz("How does Mina handle uncertainty?", "She requests a demonstration politely.", "She agrees while concealing her confusion.", "She accuses the vendor of dishonesty.", "She asks whether he could demonstrate the amount."),
                 quiz("What does by placing… express?", "The method used to make the amount clear", "A condition that did not occur", "A criticism of the vendor", "By + -ing describes the means of achieving the result."),
                 quiz("Which claim would go beyond the passage?", "Every vendor responds positively to every question.", "This vendor demonstrates the amount.", "Mina's question supports understanding.", "One fictional exchange cannot support a universal claim about every vendor.")],
                "How can a speaker acknowledge uncertainty while keeping a conversation comfortable?",
                ["Rephrase Mina's request for an informal market visit and a formal workplace discussion.", "Explain what this scenario suggests about communication, and what it cannot establish."]),
        },
    },
]
