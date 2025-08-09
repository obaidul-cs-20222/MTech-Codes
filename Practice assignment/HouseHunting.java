import java.util.Scanner;

public class HouseHunting {

    /* -------- Task 1A: Basic calculation without salary changes -------- */
    public static int monthsToSaveBasic(double annualIncome, double saveFraction, double homePrice) {
        final double downPercent = 0.25;
        final double annualReturn = 0.04;

        double downPayment = homePrice * downPercent;
        double savings = 0.0;
        double monthlyIncome = annualIncome / 12.0;
        int monthCount = 0;

        while (savings < downPayment) {
            savings += savings * (annualReturn / 12.0);
            savings += monthlyIncome * saveFraction;
            monthCount++;
        }
        return monthCount;
    }

    /* -------- Task 1B: With semi-annual salary increases -------- */
    public static int monthsToSaveWithRaise(double annualIncome, double saveFraction, double homePrice, double raiseFraction) {
        final double downPercent = 0.25;
        final double annualReturn = 0.04;

        double downPayment = homePrice * downPercent;
        double savings = 0.0;
        double monthlyIncome = annualIncome / 12.0;
        int monthCount = 0;

        while (savings < downPayment) {
            savings += savings * (annualReturn / 12.0);
            savings += monthlyIncome * saveFraction;
            monthCount++;
            if (monthCount % 6 == 0) {
                monthlyIncome += monthlyIncome * raiseFraction;
            }
        }
        return monthCount;
    }

    /* -------- Task 1C: Find optimal saving rate via bisection search -------- */
    public static double optimalSavingsRate(double annualIncome, double homePrice) {
        final double downPercent = 0.25;
        final double annualReturn = 0.04;
        final double raiseFraction = 0.07;
        final int targetMonths = 36;
        final double tolerance = 100.0;

        double downPayment = homePrice * downPercent;
        int low = 0, high = 10000;
        int stepCount = 0;

        while (low <= high) {
            stepCount++;
            int mid = (low + high) / 2;
            double rate = mid / 10000.0;
            double savings = 0.0;
            double monthlyIncome = annualIncome / 12.0;

            for (int month = 1; month <= targetMonths; month++) {
                savings += savings * (annualReturn / 12.0);
                savings += monthlyIncome * rate;
                if (month % 6 == 0) {
                    monthlyIncome += monthlyIncome * raiseFraction;
                }
            }

            if (Math.abs(savings - downPayment) <= tolerance) {
                System.out.println("Steps in bisection search: " + stepCount);
                return rate;
            } else if (savings < downPayment) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1; // not achievable
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Select mode: 1A, 1B, or 1C");
        String choice = scanner.nextLine().trim();

        switch (choice.toUpperCase()) {
            case "1A":
                System.out.print("Annual salary: ");
                double salaryA = scanner.nextDouble();
                System.out.print("Portion saved (decimal): ");
                double saveA = scanner.nextDouble();
                System.out.print("Home cost: ");
                double priceA = scanner.nextDouble();
                System.out.println("Months required: " + monthsToSaveBasic(salaryA, saveA, priceA));
                break;

            case "1B":
                System.out.print("Annual salary: ");
                double salaryB = scanner.nextDouble();
                System.out.print("Portion saved (decimal): ");
                double saveB = scanner.nextDouble();
                System.out.print("Home cost: ");
                double priceB = scanner.nextDouble();
                System.out.print("Semi-annual raise (decimal): ");
                double raiseB = scanner.nextDouble();
                System.out.println("Months required: " + monthsToSaveWithRaise(salaryB, saveB, priceB, raiseB));
                break;

            case "1C":
                System.out.print("Annual salary: ");
                double salaryC = scanner.nextDouble();
                System.out.print("Home cost: ");
                double priceC = scanner.nextDouble();
                double rate = optimalSavingsRate(salaryC, priceC);
                if (rate < 0) {
                    System.out.println("It is not possible to save enough in 36 months.");
                } else {
                    System.out.printf("Best savings rate: %.4f\n", rate);
                }
                break;

            default:
                System.out.println("Invalid selection.");
        }

        scanner.close();
    }
}
