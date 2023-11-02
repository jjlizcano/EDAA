public class Test
{
    public static void main(String[] args)
    {

        MergeSort mergeSort = new MergeSort();
        System.out.println("Ingrese el tamaño del arreglo: ");
        int elements = Integer.parseInt(System.console().readLine());
        while (elements <= 0)
        {
            System.out.println("Ingrese un número mayor a 0: ");
            elements = Integer.parseInt(System.console().readLine());
        }
        int arr [] = new int[elements];
        for (int i = 0; i < elements; i++)
        {
            System.out.println("Ingrese el elemento " + (i+1) + ": ");
            arr[i] = Integer.parseInt(System.console().readLine());
        }
        int n = arr.length;

        System.out.println("Array original:");
        for (int value : arr)
        {
            System.out.print(value + " ");
        }

        System.out.println();

        System.out.println("Array ordenado:");
        mergeSort.sort(arr, 0, n-1);
        mergeSort.printArray(arr);
    }
}

// El programa no funcionó con flotantes ni validó que no hubiera letras. Arrepentido de no haberlo hecho.