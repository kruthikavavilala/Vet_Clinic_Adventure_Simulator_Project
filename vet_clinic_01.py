
name = input("What is your name?: ")

print("Hello " + name + " We are going to have so much fun today in our vet simulator")

animal = input("There are three animals that need help today. However, you can only pick one.\n Do you want to pick the cat, the dog or the horse? ")

print("animal:", animal )

score = 0

print("Your starting score right now is zero!")

if animal.strip().lower() == "cat":
    print("Nice choice. Now you will have to answer 5 questions that will help that cat. ")
    cat1 = input("Question 1. If your cat has a severe cough and a high fever, what is the safest immediate action?\nA) Give them a small, safe dose of children's liquid fever reducer to bring the temperature down safely.\nB) Run a hot shower to create a steam room for 15 minutes to clear the lungs while you call the vet.\nC) Keep them cool with ice packs wrapped in towels and wait 24 hours to see if the fever breaks naturally. ")
    if cat1.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif cat1.strip().lower() != "b":
        print("Incorrect!")

    cat2 = input("Question 2. You suspect your cat has a fever. What is the most accurate way to check their temperature before calling the vet?\nA) Feel the tips of their ears and the pads of their paws to see if they feel unusually hot.\nB) Check if their nose is completely dry and warm, which confirms a high internal temperature.\nC) Use a digital pediatric thermometer rectally with a safe lubricant for an exact reading.")
    if cat2.strip().lower() == "c":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif cat2.strip().lower() != "c":
        print("Incorrect!")

    cat3 = input("Question 3. Your cat has a runny nose and is sneezing. How can you tell the difference between a mild cat cold and a severe respiratory infection that needs a vet?\nA) A mild cold only causes clear discharge, while a severe infection always causes green or yellow mucus.\nB) A mild cold will resolve on its own in 48 hours, whereas a severe infection lasts longer than two days.\nC) A mild cold doesn't affect their appetite or energy, but a severe infection makes them stop eating and become very tired.")
    if cat3.strip().lower() == "c":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif cat3.strip().lower() != "c":
        print("Incorrect!")

    cat4 = input("Question 4. If a cat is suffering from a fever, why is it dangerous to simply let them sleep it off over the weekend?\nA) Cats with fevers stop drinking water and can develop life-threatening dehydration very quickly.\nB) A fever will cause the cat's internal body temperature to permanently reset to a higher, dangerous level.\nC) Sleeping too much with a fever causes fluid to immediately pool in their stomach and lungs.")
    if cat4.strip().lower() == "a":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif cat3.strip().lower() != "a":
        print("Incorrect!")

    cat5 = input("Question 5. What is the primary reason why common human pain relievers (like Tylenol) are deadly to a sick cat?\nA) They thin the cat's blood too much, causing sudden and severe internal bleeding.\nB) The cat's liver cannot break down the medication, causing fatal organ failure from a single pill.\nC) They cause a sudden drop in blood pressure that makes the cat faint and go into a coma.")
    if cat5.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif cat3.strip().lower() != "b":
        print("Incorrect!")


if animal.strip().lower() == "dog":
    print("Nice choice. Now you will have to answer 5 questions that will help that dog. ")
    dog1 = input("Question 1. Your dog has developed a deep, rattling cough alongside a dangerously high temperature. What is the safest immediate step you should take?\nA) Administer a tiny dose of over-the-counter pediatric fever medication to safely bring their temperature down.\nB) Bring the dog into a closed bathroom with a running hot shower to let the steam soothe their lungs while calling the clinic.\nC) Press wrapped frozen gel packs against their stomach and groin, then wait a full day to see if the fever breaks naturally.")
    if dog1.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif dog1.strip().lower() != "b":
        print("Incorrect!")

    dog2 = input("Question 2. Your dog is suffering from a runny nose and frequent sneezing. How can you tell if they just have a simple case of seasonal allergies or a severe respiratory emergency?\nA) Basic allergies only cause clear fluid to run from the nose, whereas a dangerous infection always produces thick yellow mucus.\nB) A simple allergy will clear up completely on its own within 48 hours, while a major infection lasts longer than two days.\nC) A mild allergy won't disrupt their mood or food drive, but a serious infection will make them refuse meals and act incredibly weak. ")
    if dog2.strip().lower() == "c":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif dog2.strip().lower() != "c":
        print("Incorrect!")

    dog3 = input("Question 3. If a dog is running a severe fever, why is it incredibly dangerous to just leave them alone to sleep it off through the weekend?\nA) Feverish dogs will completely refuse to drink and can suffer from life-threatening dehydration in a very short window of time.\nB) Leaving a fever untreated causes the dog's internal biological thermostat to permanently lock itself at a higher, lethal baseline.\nC) Excessive sleeping while feverish forces fluid to immediately collect inside the dog's stomach cavity and lung chambers.")
    if dog3.strip().lower() == "a":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif dog3.strip().lower() != "a":
        print("Incorrect!")

    dog4 = input("Question 4. You are worried that your dog might be running a fever. What is the only scientifically accurate way to check their temperature before calling your veterinarian?\nA) Gently feel the tips of their ears and their paw pads to see if they radiate an unusual amount of heat.\nB) Touch the tip of their snout to see if it is completely dry and warm, which confirms a spiking temperature.\nC) Insert a digital pediatric thermometer rectally with a pet-safe lubricant to get an exact internal measurement.")
    if dog4.strip().lower() == "c":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif dog4.strip().lower() != "c":
        print("Incorrect!")

    dog5 = input("Question 5. What is the primary biological reason why giving a dog a common human pain reliever like Tylenol is so incredibly lethal?\nA) The active ingredients thin the canine bloodstream so severely that the dog will suffer sudden, uncontrollable internal bleeding.\nB) A dog's liver lacks the mechanics to process the drug, causing the medication to rapidly destroy the organ's cells.\nC) The pill causes an instantaneous crash in the dog's blood pressure, sending them into a deep, unresolvable coma.")
    if dog5.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif dog5.strip().lower() != "b":
        print("Incorrect!")


if animal.strip().lower() == "horse":
    print("Nice choice. Now you will have to answer 5 questions that will help that horse. ")
    horse1 = input("Your horse is displaying clear signs of colic (severe abdominal pain) by pawing the ground, looking at their flanks, and trying to roll. While waiting for the vet, what is the most critical rule regarding walking the horse?\nA) You must continuously force the horse to trot or run for at least 45 minutes to manually force the gas or blockage to break apart.\nB) You should only walk the horse if they are actively trying to thrash and roll violently, as rolling can cause a fatal twisted intestine.\nC) You must keep the horse absolutely still and tied to a hitching post so that movement doesn’t accelerate their heart rate.")
    if horse1.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif horse1.strip().lower() != "b":
        print("Incorrect!")

    horse2 = input("Question 2 Your horse is standing in the pasture and suddenly starts coughing violently, gagging, and thick green saliva mixed with chewed grain starts pouring out of both nostrils. What is happening, and what is the immediate veterinary protocol?\nA) The horse is suffocating because food is blocked in their windpipe; you must immediately perform an emergency tracheotomy.\nB) The horse is throwing up stomach acid from a ruptured ulcer; you must immediately drench them with liquid antacids.\nC) The horse has choke meaning food is stuck in their esophagus (food pipe); you must remove all food and water immediately and call the vet.")
    if horse2.strip().lower() == "c":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif horse2.strip().lower() != "c":
        print("Incorrect!")

    horse3 = input("Question 3. A horse accidentally breaks into the grain room and eats an entire 50-pound bag of sweet feed. Even if the horse looks completely fine right now, why is this an immediate, life-threatening veterinary emergency?\nA) The massive sugar spike causes a toxic bacterial bloom in the hindgut, which releases endotoxins that cause laminitis (founder), destroying the hooves.\nB) The sheer weight of the dry grain will cause the horse's stomach to instantly flip upside down, cutting off all blood flow to the heart.\nC) The molasses in sweet feed permanently coats the lining of the stomach, preventing the horse from ever absorbing nutrients again.")
    if horse3.strip().lower() == "a":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif horse3.strip().lower() != "a":
        print("Incorrect!")

    horse4 = input("Question 4. Your horse cuts their leg on a fence. The wound is on the lower leg, right over a joint. It is barely bleeding and looks like a tiny, harmless puncture wound. Why do vets consider a tiny puncture over a joint much more dangerous than a large, bleeding flesh cut on the neck?\nA) Lower leg skin has a direct chemical reaction to air that transforms minor bacteria into flesh-eating viruses.\nB) Tiny punctures trap bacteria deep inside the sterile joint fluid, causing a rapid, destructive infection that can permanently ruin the joint.\nC) The lower leg lacks any blood pressure, meaning the body's immune system cannot send white blood cells down to heal a puncture.")
    if horse4.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif horse4.strip().lower() != "b":
        print("Incorrect!")

    horse5 = input("Question 5. When a horse suffers a severe injury to its lower leg, a strange, bright red, bumpy tissue that looks like raw hamburger meat can start aggressively growing out of the wound, preventing the skin from healing. What is this veterinary condition called?\nA) Necrotic Slough\nB) Proud Flesh\nC) Fibrotic Myositis")
    if horse5.strip().lower() == "b":
        print("Correct!")
        score = score + 10
        print("Your current score is " , score)
    elif horse5.strip().lower() != "b":
        print("Incorrect!")



if score == 50:
    print("A perfect score 50/50 💯. Are you secretly a veterinarian already?! The test should be studying you.")

if score == 40:
    print(" 40/50 - Wow! You know your stuff. Just 1 sneaky question got away.")

if score == 30:
    print("Not bad! Yow got a 30/50. You're halfway between beginner and expert.The animals approve. Mostly.")

if score == 20:
    print("20/50 - Okay, we need a little more studying. The bacteria beat you, but only this time.")

if score == 10:
    print("10/50 - The test wasn't a fan, but at least 1 answer believed in you. The good news: double digits!")

if score == 0:
    print("0/50 - Well... at least you were consistent🤣🤣. And you got your name correct.")



    

