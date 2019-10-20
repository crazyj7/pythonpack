
# Jake Cipher

This encryption algorithm is based in Affine encryption and Ultari encryption.

Complex encryption algorithm using affine password and fence cipher

=> Don't encrypt spaces, numbers, or special characters.  
=> Apply encryption only sequentially to the alphabet.  
=> 26 character codes are used, uppercase letters are encrypted and lowercase letters are encrypted.  

The key is N in pairs of two affine keys. In addition, add another fence encryption key.
The key pair has a product key and a sum key, so the input value is multiplied by the corresponding value and the sum key is added.
After the affine password, the fence cipher creates a row corresponding to the key value and transposes the data.
The character set used for encryption is a 26-character alphabet and is modulated by a mod 26 operation on the operation value.



아핀암호와 울타리 암호를 응용한 복합 암호화 알고리즘  

=> 공백, 숫자, 특수문자는 암호화 하지 않는다.  
=> 알파벳에만 암호화를 순차적으로 적용한다.  
=> 문자코드는 26개를 사용하며 대문자는 대문자 암호화, 소문자는 소문자로 암호화한다.

키는 아핀키 두 개를 쌍으로 하여 N개를 사용한다. 추가로 울타리 암호키를 하나 더 추가한다.   
키 쌍은 곱 키와 합 키가 있어서 입력값에 해당 값을 곱한 후 합 키를 더한다.  
아핀 암호 후에 울타리 암호로 키값에 해당되는 row를 만들어 데이터를 transpose(전치)한다.
암호화에 사용되는 문자셋은 알파벳 26자로 연산값에 mod 26 연산을 하여 다시 문자로 치환한다.  
