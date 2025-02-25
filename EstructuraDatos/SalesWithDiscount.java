public class SalesWithDiscount {
    
    public double totalWithDiscount() {
            double[] sales = {100.0, 200.0, 150.0, 300.0};
            double total = 0.0;
            
            System.out.println("Arreglo de ventas:");
            for (double sale : sales) {
                System.out.print(sale + " ");
            }
            System.out.println("\nCálculos individuales con descuento:");
            
            for (double sale : sales) {
                double discountedSale = sale * 0.9;
                System.out.println(sale + " * 0.9 = " + discountedSale);
                total += discountedSale;
            }
            
            return total;
        }
        
        public static void main(String[] args) {
            SalesWithDiscount salesCalculator = new SalesWithDiscount();
            double total = salesCalculator.totalWithDiscount();
            System.out.println("La suma total de ventas con el 10% de descuento es: " + total);
        }
    }
    

