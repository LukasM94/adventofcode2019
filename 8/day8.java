import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day8 {

	public static void main(String[] args) throws FileNotFoundException {
		// reading file
		File file = new File("input.txt");
		Scanner sc = new Scanner(file);

		//Put file to string
		String input = sc.nextLine();
		sc.close();

		int img_width=25;
		int img_height=6;

		int img_size= img_width*img_height;

		int layers = input.length()/img_size;

		System.out.println("There are " + layers + " layers.");

		//Image array = layer_numb, height, width

		int[][][] image = new int[layers][img_height][img_width];

		//Parse image to array

		for (int layer =0; layer<layers; layer++) {
			for (int height=0; height<img_height; height++) {
				for (int width=0; width<img_width; width++) {
					int pointer = (layer*img_size)+(height*img_width)+width;
					image[layer][height][width] = Character.getNumericValue(input.charAt(pointer));
				}
			}
		}

		int checksum_layer = layerWithFewestZeroes(image, layers, img_width, img_height);

		System.out.println("Fewest number of zeroes is on layer " + checksum_layer);

		System.out.println("Checksum is "
		+ calculateImageChecksum(image, checksum_layer, img_width, img_height));

		int [][] finalImage = decodeImage(image, layers, img_width, img_height);

		System.out.println("Here is final image:");
		printImage(finalImage, img_width, img_height);

	}

	static int layerWithFewestZeroes(int[][][] image, int layers, int img_width, int img_height) {
		int minNumberOfZeroes=99999;
		int layerWithFewestZeroes=-1;

		for (int layer =0; layer<layers; layer++) {
			int zeroes=0;
			for (int height=0; height<img_height; height++) {
				for (int width=0; width<img_width; width++) {
					if (image[layer][height][width]==0) {
						zeroes++;
					}
				}
			}

			if (zeroes < minNumberOfZeroes) {
				layerWithFewestZeroes=layer;
				minNumberOfZeroes=zeroes;
			}
		}

		return layerWithFewestZeroes;
	}

	static int calculateImageChecksum(int[][][] image, int layer, int img_width, int img_height) {
		int numberOfOnes=0;
		int numberOfTwos=0;

		for (int height=0; height<img_height; height++) {
			for (int width=0; width<img_width; width++) {
				if (image[layer][height][width]==1) {
					numberOfOnes++;
				}
				if (image[layer][height][width]==2) {
					numberOfTwos++;
				}
			}
		}

		return numberOfOnes*numberOfTwos;
	}

	static int[][] decodeImage (int[][][] image, int layers, int img_width, int img_height) {
		int[][] finalImage = new int[img_height][img_width];

		for (int width=0; width<img_width; width++) {
			for (int height=0; height<img_height; height++) {
				for (int layer=0; layer<layers; layer++) {
					if (image[layer][height][width]!=2) {
						finalImage[height][width]=image[layer][height][width];
						System.out.println(width + " " + height + " " + layer);
						break;
					}
				}
			}
		}

		return finalImage;
	}

	static void printImage(int[][] image, int img_width, int img_height) {
		for (int height=0; height<img_height; height++) {
			for (int width=0; width<img_width; width++) {
				if (image[height][width]==0) {
					 System.out.print(' ');
				} if (image[height][width]==1) {
					 System.out.print('X');
				}
			}
			System.out.print('\n');
		}
	}
}
