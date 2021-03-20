package trigonometry;

import java.util.Scanner;

public class Trigonometry {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Type '?commands' for the list of commands ");
        boolean run = true;
        OUTER:
        while (run) {
            String user = input.nextLine();
            switch (user) {
                case "?commands":
                    System.out.println("Here is the list of Commands:");
                    String[] commands = new String[8]; //amount of commands
                    commands[0] = "?sine law - gives the equation for sine law"; //command list
                    commands[1] = "?cosine law - gives the equation for cosine law; both for missing angle and side length";
                    commands[2] = "?sine law cal - given SSA returns missing angle, given SAA returns missing side length";
                    commands[3] = "?cosine law cal - given SSS returns all angles, given SAS returns missing side length";
                    commands[4] = "?pythagorean - gives the pythagorean theorem";
                    commands[5] = "?pythagorean cal - given side a and b, returns side c";
                    commands[6] = "?trigonometric ratios";
                    commands[7] = "no u";
                    for (int i = 0; i < commands.length; i++) {
                        System.out.println(i + 1 + ". " + commands[i]);
                    }
                    break;
                case "?sine law":
                    System.out.println("SinA/a = SinB/b = SinC/c");
                    break;
                case "?cosine law":
                    System.out.println("For missing side length: c^2 = a^2 + b^2 – 2ab * cos C");
                    System.out.println("For missing angle: cos C = (a^2 + b^2 − c^2)/2ab");
                    break;
                case "?sine law cal":
                    System.out.println("Type 1 to find a missing side length, Type 2 to find a missing angle");
                    String select = input.nextLine();
                    switch (select) {
                        case "1": {
                            //Calculates missing side length using Sine Law
                            System.out.println("Type in angle A, side b, and angle B to find side a");
                            double aa = input.nextDouble();
                            double sb = input.nextDouble();
                            double ab = input.nextDouble();
                            double sa = sb * Math.sin(Math.toRadians(aa)) / Math.sin(Math.toRadians(ab));
                            System.out.println("Side a is equal to " + sa + " units");
                            break;
                        }
                        case "2": {
                            //Calculates missing angle using Sine Law
                            System.out.println("Type in side a, angle B, and side b to find angle A");
                            double sa = input.nextDouble();
                            double ab = input.nextDouble();
                            double sb = input.nextDouble();
                            double aa = Math.toDegrees(Math.asin(sa * Math.sin(Math.toRadians(ab)) / sb));
                            System.out.println("Angle A is equal to " + aa + " degrees");
                            break;
                        }
                        default:
                            System.out.println("Please select 1 or 2");
                            break;
                    }
                    break;
                case "?pythagorean": {
                    //gives pythagorean theorem
                    System.out.println("a^2 + b^2 = c^2" + " OR " + "c = sqrt(a^2 + b^2)");
                    break;
                }
                case "?pythagorean cal": {
                    //calculates side c using pythagorean theorem
                    System.out.println("Enter side a and side b to get side c");
                    double a = input.nextDouble();
                    double b = input.nextDouble();
                    System.out.println("Side c is equal to " + Math.sqrt((Math.pow(a, 2)) + Math.pow(b, 2)) + " units");
                    break;
                }
                case "?cosine law cal": {
                    System.out.println("Enter 1 to find a missing angle, Enter 2 to find a missing side length, Enter 3 to solve all");
                    String enter = input.nextLine();
                    switch (enter) {
                        case "1": {
                            System.out.println("Please enter side a, side b, and side c");
                            double sa = input.nextDouble();
                            double sb = input.nextDouble();
                            double sc = input.nextDouble();
                            double ac = Math.toDegrees(Math.acos((Math.pow(sa, 2) + Math.pow(sb,2) - Math.pow(sc,2)) / (2 * sb * sa)));
                            System.out.println("Angle C is equal to " + ac + " degrees");
                            break; //break doesn't work
                        }
                        case "2": {
                            System.out.println("Please enter side a, side b, and angle c");
                            double sa = input.nextDouble();
                            double sb = input.nextDouble();
                            double ac = input.nextDouble();
                            double sc = Math.sqrt(Math.pow(sa, 2) + Math.pow(sb, 2) - 2 * sa * sb * Math.cos(Math.toRadians(ac)));
                            System.out.println("Side c is equal to " + sc + " units");
                            break; //break doesn't work
                        }
                        case "3": {
                            //solves the triangle
                        }
                        default:
                            System.out.println("Please enter 1 or 2");
                            break;
                            
                    }
                }
                case "Stop":
                    break OUTER;
                default:
                    break;
            }
        }
    }

}
