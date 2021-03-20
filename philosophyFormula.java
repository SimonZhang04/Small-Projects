package the.philosophy.formula;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        long startTime = System.nanoTime();
        Scanner input = new Scanner(System.in);
        System.out.println("The Philosophy Formula: Literary Theorem by Simon Zhang");
        System.out.println("Philosophy: noun");
        System.out.println("The study of the fundamental nature of knowledge, reality, existence, and thought.");
        System.out.println("__________________________________________________");
        while (true) {
            for (int i = 0; i < 2; i++) {
                System.out.println();
            }
            System.out.println("For more information about philosophy, enter 1...");
            System.out.println("For the list of all stages and paths, enter 2...");
            System.out.println("To create your own path, enter 3...");
            System.out.println("To quit the program, enter 0...");
            System.out.println("__________________________________________________");
            int start = input.nextInt();
            switch (start) {
                case 1: {
                    System.out.println();
                    System.out.println("Philosophy, comes from the Greek word “phílosophía” meaning ‘the love of wisdom’");
                    System.out.println("It is the study of knowledge, and thinking about 'thinking.'");
                    System.out.println("Philosopical questions are mostly foundational and abstract in nature, and can found in many forms.");
                    System.out.println("It provides a good way of learning to think more clearly about greater variety of topics; its methods used to analyze a situation can also we useful in other areas.");
                    System.out.println();
                    System.out.println("Categories of Philosophy");
                    System.out.println("Philosophy can be split into many different categories, but it is most commonly divided by geographics, branches, and historical period.");
                    System.out.println();
                    System.out.println("Geographical:");
                    System.out.println("Eastern Philosophy");
                    System.out.println("Western Philosophy");
                    System.out.println("African Philosophy (as possible 3rd branch)");
                    System.out.println();
                    System.out.println("Historical Period:");
                    System.out.println("Ancient");
                    System.out.println("Medieval");
                    System.out.println("Modern");
                    System.out.println();
                    System.out.println("Branches:");
                    System.out.println("Metaphysics: Study of existence and the nature of reality");
                    System.out.println("Epistemology: Study of knowledge and how and what we know");
                    System.out.println("Ethics: Study of how people should act, what is good and valuable");
                    System.out.println("Aesthetics: Study of basic philosophical questions about art and beauty");
                    System.out.println("Include many additional branches...");
                    System.out.println("Logic, Political, Education, Religion, History, Language, Science, Law, Sociology, Mathematics, Ethnology, Psychology, and Meta-Philosophy");
                    System.out.println();
                    System.out.println("To go back to menu, enter any character");
                    System.out.println("__________________________________________________");
                    String any = input.nextLine();
                    String any1 = input.nextLine();
                    break;
                }
                case 3: {
                    System.out.println("Create your own path of Philosophy by selecting a path from each stage to create a journey.");
                    System.out.println();
                    System.out.println();
                    int[] paths = new int[4];
                    System.out.println("Stage 1: Triggering a Realization");
                    System.out.println("To select a path enter the number assigned to each path.");
                    System.out.println();
                    System.out.println("1. Wandering Mind");
                    System.out.println("2. Self Reflection/Thinking about the Future");
                    System.out.println("3. Inspiration");
                    System.out.println("4. Dilemma/Predicament");
                    System.out.println("5. Argument");
                    System.out.println("6. Why?");
                    System.out.println("7. Peculiar Event");
                    System.out.println("__________________________________________________");
                    paths[0] = input.nextInt();
                    System.out.println();
                    System.out.println("Stage 2: Pondering the Question");
                    System.out.println("To select a path enter the number assigned to each path.");
                    System.out.println();
                    System.out.println("8. Logical Reasoning");
                    System.out.println("9. Modifying the Question");
                    System.out.println("10. Experimentation");
                    System.out.println("11. Creating a Situation");
                    System.out.println("__________________________________________________");
                    paths[1] = input.nextInt();
                    System.out.println();
                    System.out.println("Stage 3: Coming to a Conclusion");
                    System.out.println("12. Developing A Theory");
                    System.out.println("13. Finding a Non-Example");
                    System.out.println("14. Catch 22");
                    System.out.println("15. One of Many Answers");
                    System.out.println("16. Revisting the Question");
                    System.out.println("__________________________________________________");
                    paths[2] = input.nextInt();
                    System.out.println();
                    System.out.println("Stage 4: Sharing the Idea");
                    System.out.println("17. Debate");
                    System.out.println("18. Asking for Opinion");
                    System.out.println("19. Using Literature");
                    System.out.println("20. Power of the Internet");
                    System.out.println("__________________________________________________");
                    paths[3] = input.nextInt();
                    System.out.println("Here are the paths you chose");
                    System.out.println();
                    System.out.println("Stage 1: Triggering the Realization");
                   
                    switch (paths[0]) {
                        case 1:
                            System.out.println("Wandering Mind");
                            System.out.println("Ideas and questions start forming in your head when outside senses are blanked out, and you stare at nothing in particular. You could be bored, auto-piloting a task, laying in bed, taking a shower, or looking outside at nature or stars. Questions may come and go, some you might think about more than others. ");
                            break;

                        case 2:
                            System.out.println("Reflection");
                            System.out.println("It is important to look beyond daily life, and something many people think about is their current situation and how they can improve themselves and their futures. Thinking about, “What is important to me?”, “What will the future look like?”, and “What do other people of me?” are questions we often ask ourselves.");
                            break;
                        case 3:
                            System.out.println("Inspiration");
                            System.out.println("An idea/opinion planted into your head from someone thinking of a similar thought. You may find the inspiration in the form of a quote, movie, book, website, or a place such as a museum or art gallery. The person who came up with the original idea may have a different or similar opinion as you do.");
                            break;
                        case 4:
                            System.out.println("Dilemma/Predicament");
                            System.out.println("Often times when we don’t know what to do in a tough or very important situation we think about our options. This forces to us to think: “Which option is the best?”, and “Should morals be considered above a better outcome?” Philosophy has shown real world application of this in Value Theory. What is most/more important is question often asked in philosophy. ");
                            break;
                        case 5:
                            System.out.println("Argument");
                            System.out.println("An argument generally is based off of who is right or wrong, and so are many philosophical topics such as morals/ethics. The conflict can spring from knowing the truth, or what option would lead to the best possible outcome. Often times, in order to prove a point we would use logic or create a similar scenario to imagine outcomes, just as a philosopher would.");
                            break;
                        case 6:
                            System.out.println("Why?");
                            System.out.println("Just like as when you were a kid, the world was a wonder that had so many unanswered questions. You might think to yourself, “Why did I stop asking questions?” or “Why is the world like what it is right now?”. Many things don’t make sense to us, but we have learned to just put up with it most of the time.");
                            break;
                        case 7:
                            System.out.println("Peculiar Event");
                            System.out.println("Something strange may have just happened to you, it could be something seemly supernatural, from a dream, or maybe it’s déjà vu. It causes you to think, “What caused that?”, “Was there a meaning behind it?”, “Why did it happen?”. The event could have also been something on a larger scale such as on the news, typically controversial topics such as gun ownership or politics. ");
                            break;
                    }
                    System.out.println();
                            System.out.println("Stage 2: Pondering the Question");
                            
                            switch (paths[1]) {
                                case 8:
                                    System.out.println("Logical Reasoning");
                                    System.out.println("Logic provides are a clear and effective understand of a subject. It is commonly used in philosophy because it expresses the nature of philosophy; that expressive thought and the application of ideas can lead to clear and useful answers. It is inherent and fundamental in every person and is often mankind’s best tool.");
                                    break;
                                case 9:
                                    System.out.println("Modifying the Question");
                                    System.out.println("The first question you think about might not at first hold a clear answer, or it might just have a boring/pointless conclusion. Asking similar or smaller related questions to break down the original question can be a effective strategy in finding a clearer, more fruitful conclusion. Using the example of Theseus’s ship, we can ask a similar question about ourselves. What if we created a clone of ourselves, or we replaces some body parts with someone else/artificial parts, or when we think about the fact that we replace all the cells in our bodies in about 10 years. It makes the connection; “Who am I?”, rather than perhaps “What is this?”");
                                    break;
                                case 10:
                                    System.out.println("Experimentation");
                                    System.out.println("In order to find a solution or test possible ones, experiments can be very useful. The only way to find if something is true is by seeing for yourself in the real world. In turn, it can show you the value of the idea in your reality. Experiments, however are generally not very common in philosophy, because of the abstract nature of philosophical questions generally more reflection is done. An example that proves experimentation useful is how it can debunk Zeno’s Paradoxes, such as Achilles and the Tortoise. However, we know in the real world, a man can certainly outrun a tortoise.");
                                    break;
                                case 11:
                                    System.out.println("Creating a Situation");
                                    System.out.println("This can help with imagining possible solutions, as there are no limits to imagination. Creating a situation can also allow you to explore different perspectives, and thinking of the question in a larger variety of ways. Many thought experiments have been proven useful; such as Maxwell’s Demon and Schrodinger's Cat in a Box. It gives us the power to create our own worlds that is our sandboxes and tool kits to finding the answer to our questions. ");
                                    break;
                            }
                            System.out.println();
                            System.out.println("Stage 3: Coming to a Conclusion");
                            
                            switch (paths[2]) {
                                case 12:
                                    System.out.println("Developing a Theory");
                                    System.out.println("A solution has been found that has proven to be logical, and with no holes. It has gone with a road of trials in validation in a variety of methods, such as experimentation, agreement with others and/or deep reflection. However, nothing can be certain. “The only certainty is that nothing is certain.” - Pliny the Elder");
                                    break;
                                case 13:
                                    System.out.println("Finding a Non-Example");
                                    System.out.println("After thinking about the question, we may be convinced we have come to a potential solution. However, we may have forgotten a detail that causes the solution to make no sense at all. This is shown in the case of Plato’s argument of how humans are categorized as birds - “featherless bipeds” what what he called them. However, Diogenes the Cynic completely disagreed and came into Plato’s class with a plucked chicken and said, “Behold, Plato’s man.”");
                                    break;
                                case 14:
                                    System.out.println("Catch 22");
                                    System.out.println("Sometimes it may be impossible to reach a explanation to the question. In order the answer the question, another question may have to be asked and it gets to an endless cycle. Maybe the question was never meant to have a solution, or the current knowledge of us restrains us from the answer, which is what we call a paradox. A simple example is this: “Is the answer to this question, no?”");
                                    break;
                                case 15:
                                    System.out.println("One of Many Answers");
                                    System.out.println("The answer to the question may be purely based off of opinion. There could be the an answer that you think is the best, and another answer that is valid, however you don’t think is as good of as an answer. What you think is the best answer may be completely different than that of someone else. There is no ‘wrong’ answer.");
                                    break;
                                case 16:
                                    System.out.println("Revisiting the Question");
                                    System.out.println("At first the question may be seemly impossible to answer, or have a useless conclusion. Maybe with the help of others, experience in the future, or further pondering could lead to a solution. Even if an answer is never reached or the question had an answer that appeared to have no value, it is important to remember that there is value is thinking. As Socrates once said - “The unexamined life is not worth living.”");
                                    break;
                            }
                            System.out.println();
                            System.out.println("Stage 4: Sharing the Idea");
                            
                            switch (paths[3]) {
                                case 17:
                                    System.out.println("Debate");
                                    System.out.println("“There is only one thing a philosopher can be relied upon to do, and that is to contradict other philosophers” said William James, an American philosopher.  Debating is something that many philosophers do, to put their theories to the test. By finding someone who disagrees with your belief, you might learn a lot about the idea in question. By disputing, you may find holes in your argument, find new ideas to reinforce your argument, or find out exactly how strong your argument is. The other person may show you a new perspective or another possible answer to your question. ");
                                    break;
                                case 18:
                                    System.out.println("Asking for Opinion");
                                    System.out.println("Unlike debating, you would ask someone about what they think about your own answer/opinion. You might work together in agreement to strengthen your points through the stages of philosophy. Instead of arguing, together you build on the logic, proof, real world application, and importance of the idea. In this case of agreement, sharing the idea can lead to more and more people acknowledging it and making them think as well.");
                                    break;
                                case 19:
                                    System.out.println("Using Literature");
                                    System.out.println("Literature is good way of being expressive with ideas, and is effective in passing an idea along to more people. It can also come in many different forms, such as books, poems, movies, articles, cartoons or videos. Picking a style that suits you and the idea can get you to create amazing literature, and retain your thoughts forever. Example: A book I have read is “Paradox: The Nine Greatest Enigmas in Physics” by Jim Al-Khalili which ties together logical thinking and physics.");
                                    break;
                                case 20:
                                    System.out.println("Power of the Internet");
                                    System.out.println("In the modern world, the technology provides an effective tool with connecting the world through the internet. Sharing online is an easy way to get others to come across your ideas. Using social media, you can easily join groups with particular interests that may relate to the topic of your idea. Examples of websites include as Reddit (r/showerthoughts) and Quora (Q&A for a variety of topics including Philosophy at www.quora.com/topic/Philosophy).");
                                    break;
                            }
                            System.out.println();
                            System.out.println("To go back to menu, enter any character");
                            System.out.println("__________________________________________________");

                            String any = input.nextLine();
                            String any1 = input.nextLine();
                            break;
                    
                }
                case 2: {
                    System.out.println("Stage 1: Triggering a Realization");
                    System.out.println();
                    System.out.println("1. Wandering Mind:");
                    System.out.println("Ideas and questions start forming in your head when outside senses are blanked out, and you stare at nothing in particular. You could be bored, auto-piloting a task, laying in bed, taking a shower, or looking outside at nature or stars. Questions may come and go, some you might think about more than others. ");
                    System.out.println();
                    System.out.println("2. Reflection");
                    System.out.println("It is important to look beyond daily life, and something many people think about is their current situation and how they can improve themselves and their futures. Thinking about, “What is important to me?”, “What will the future look like?”, and “What do other people of me?” are questions we often ask ourselves.");
                    System.out.println();
                    System.out.println("3. Inspiration:");
                    System.out.println("An idea/opinion planted into your head from someone thinking of a similar thought. You may find the inspiration in the form of a quote, movie, book, website, or a place such as a museum or art gallery. The person who came up with the original idea may have a different or similar opinion as you do.");
                    System.out.println();
                    System.out.println("4. Dilemma/Predicament:");
                    System.out.println("Often times when we don’t know what to do in a tough or very important situation we think about our options. This forces to us to think: “Which option is the best?”, and “Should morals be considered above a better outcome?” Philosophy has shown real world application of this in Value Theory. What is most/more important is question often asked in philosophy. ");
                    System.out.println();
                    System.out.println("5. Argument:");
                    System.out.println("An argument generally is based off of who is right or wrong, and so are many philosophical topics such as morals/ethics. The conflict can spring from knowing the truth, or what option would lead to the best possible outcome. Often times, in order to prove a point we would use logic or create a similar scenario to imagine outcomes, just as a philosopher would.");
                    System.out.println();
                    System.out.println("6. Why?:");
                    System.out.println("Just like as when you were a kid, the world was a wonder that had so many unanswered questions. You might think to yourself, “Why did I stop asking questions?” or “Why is the world like what it is right now?”. Many things don’t make sense to us, but we have learned to just put up with it most of the time.");
                    System.out.println();
                    System.out.println("7. Peculiar Event:");
                    System.out.println("Something strange may have just happened to you, it could be something seemly supernatural, from a dream, or maybe it’s déjà vu. It causes you to think, “What caused that?”, “Was there a meaning behind it?”, “Why did it happen?”. The event could have also been something on a larger scale such as on the news, typically controversial topics such as gun ownership or politics. ");
                    System.out.println();
                    System.out.println("Enter any character to continue to the next stage...");
                    System.out.println("__________________________________________________");
                    String whatever = input.nextLine();
                    String whatever1 = input.nextLine();
                    System.out.println();
                    System.out.println();
                    System.out.println("Stage 2: Pondering the Question");
                    System.out.println();
                    System.out.println("8. Logical Reasoning:");
                    System.out.println("Logic provides are a clear and effective understand of a subject. It is commonly used in philosophy because it expresses the nature of philosophy; that expressive thought and the application of ideas can lead to clear and useful answers. It is inherent and fundamental in every person and is often mankind’s best tool.");
                    System.out.println();
                    System.out.println("9. Modifying the Question:");
                    System.out.println("The first question you think about might not at first hold a clear answer, or it might just have a boring/pointless conclusion. Asking similar or smaller related questions to break down the original question can be a effective strategy in finding a clearer, more fruitful conclusion. Using the example of Theseus’s ship, we can ask a similar question about ourselves. What if we created a clone of ourselves, or we replaces some body parts with someone else/artificial parts, or when we think about the fact that we replace all the cells in our bodies in about 10 years. It makes the connection; “Who am I?”, rather than perhaps “What is this?”");
                    System.out.println();
                    System.out.println("10. Experimentation:");
                    System.out.println("In order to find a solution or test possible ones, experiments can be very useful. The only way to find if something is true is by seeing for yourself in the real world. In turn, it can show you the value of the idea in your reality. Experiments, however are generally not very common in philosophy, because of the abstract nature of philosophical questions generally more reflection is done. An example that proves experimentation useful is how it can debunk Zeno’s Paradoxes, such as Achilles and the Tortoise. However, we know in the real world, a man can certainly outrun a tortoise.");
                    System.out.println();
                    System.out.println("11. Creating a Situation:");
                    System.out.println("This can help with imagining possible solutions, as there are no limits to imagination. Creating a situation can also allow you to explore different perspectives, and thinking of the question in a larger variety of ways. Many thought experiments have been proven useful; such as Maxwell’s Demon and Schrodinger's Cat in a Box. It gives us the power to create our own worlds that is our sandboxes and tool kits to finding the answer to our questions. ");
                    System.out.println();
                    System.out.println("Enter any character to continue to the next stage...");
                    System.out.println("__________________________________________________");
                    String whateveh = input.nextLine();
                    System.out.println();
                    System.out.println();
                    System.out.println("Stage 3: Coming to a Conclusion");
                    System.out.println();
                    System.out.println("12. Developing A Theory:");
                    System.out.println("A solution has been found that has proven to be logical, and with no holes. It has gone with a road of trials in validation in a variety of methods, such as experimentation, agreement with others and/or deep reflection. However, nothing can be certain. “The only certainty is that nothing is certain.” - Pliny the Elder");
                    System.out.println();
                    System.out.println("13. Finding a Non-Example:");
                    System.out.println("After thinking about the question, we may be convinced we have come to a potential solution. However, we may have forgotten a detail that causes the solution to make no sense at all. This is shown in the case of Plato’s argument of how humans are categorized as birds - “featherless bipeds” what what he called them. However, Diogenes the Cynic completely disagreed and came into Plato’s class with a plucked chicken and said, “Behold, Plato’s man.”");
                    System.out.println();
                    System.out.println("14. Catch 22:");
                    System.out.println("Sometimes it may be impossible to reach a explanation to the question. In order the answer the question, another question may have to be asked and it gets to an endless cycle. Maybe the question was never meant to have a solution, or the current knowledge of us restrains us from the answer, which is what we call a paradox. A simple example is this: “Is the answer to this question, no?”");
                    System.out.println();
                    System.out.println("15. One of Many Answers:");
                    System.out.println("The answer to the question may be purely based off of opinion. There could be the an answer that you think is the best, and another answer that is valid, however you don’t think is as good of as an answer. What you think is the best answer may be completely different than that of someone else. There is no 'wrong' answer");
                    System.out.println();
                    System.out.println("16. Revisting the Question:");
                    System.out.println("At first the question may be seemly impossible to answer, or have a useless conclusion. Maybe with the help of others, experience in the future, or further pondering could lead to a solution. Even if an answer is never reached or the question had an answer that appeared to have no value, it is important to remember that there is value is thinking. As Socrates once said - “The unexamined life is not worth living.”");
                    System.out.println();
                    System.out.println("Enter any character to continue to the next stage...");
                    System.out.println("__________________________________________________");
                    String whatev = input.nextLine();
                    System.out.println();
                    System.out.println();
                    System.out.println("Stage 4: Sharing The Idea");
                    System.out.println();
                    System.out.println("17. Debate:");
                    System.out.println("“There is only one thing a philosopher can be relied upon to do, and that is to contradict other philosophers” said William James, an American philosopher.  Debating is something that many philosophers do, to put their theories to the test. By finding someone who disagrees with your belief, you might learn a lot about the idea in question. By disputing, you may find holes in your argument, find new ideas to reinforce your argument, or find out exactly how strong your argument is. The other person may show you a new perspective or another possible answer to your question. ");
                    System.out.println();
                    System.out.println("18. Asking for Opinion:");
                    System.out.println("Unlike debating, you would ask someone about what they think about your own answer/opinion. You might work together in agreement to strengthen your points through the stages of philosophy. Instead of arguing, together you build on the logic, proof, real world application, and importance of the idea. In this case of agreement, sharing the idea can lead to more and more people acknowledging it and making them think as well.");
                    System.out.println();
                    System.out.println("19. Using Literature:");
                    System.out.println("Literature is good way of being expressive with ideas, and is effective in passing an idea along to more people. It can also come in many different forms, such as books, poems, movies, articles, cartoons or videos. Picking a style that suits you and the idea can get you to create amazing literature, and retain your thoughts forever. Example: A book I have read is “Paradox: The Nine Greatest Enigmas in Physics” by Jim Al-Khalili which ties together logical thinking and physics.");
                    System.out.println();
                    System.out.println("20. Power of the Internet:");
                    System.out.println("In the modern world, the technology provides an effective tool with connecting the world through the internet. Sharing online is an easy way to get others to come across your ideas. Using social media, you can easily join groups with particular interests that may relate to the topic of your idea. Examples of websites include as Reddit (r/showerthoughts) and Quora (Q&A for a variety of topics including Philosophy at www.quora.com/topic/Philosophy).");
                    System.out.println();
                    System.out.println("To go back to menu, enter any character");
                    System.out.println("__________________________________________________");
                    String any1 = input.nextLine();

                    break;
                }
                case 0: {
                    long endTime = System.nanoTime();
                    long totalTime = endTime - startTime;
                    double seconds = (double) totalTime / 1000000000.0;
                    System.out.println("Congratulations,");
                    System.out.println("you spent " + Math.round(seconds) + " seconds studying Meta-Philosophy.");
                    System.out.println("“There is only one good, knowledge, and one evil, ignorance.” – Socrates");
                    System.exit(0);
                }

            }
        }
    }
}
