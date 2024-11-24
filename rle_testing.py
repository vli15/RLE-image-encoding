import rle_program
import console_gfx
if __name__ == '__main__':
    # cr = rle_program.count_runs([])
    # print("count_runs:", cr)
    # hex_string = rle_program.to_hex_string([15, 15, 15, 4, 4, 4, 4, 4, 3, 3])
    # print("hex_string:", hex_string)
    # encode_rle = rle_program.encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4, 10, 10])
    # print(encode_rle)
    # print("get decoded length:", rle_program.get_decoded_length([3,15,6,4]))
    # print("decode_rle:", rle_program.decode_rle([3,15,6,4]))
    # print("string to data:", rle_program.string_to_data('3f64'))
    # print(rle_program.to_rle_string([10,15,6,4]))
    # print("string_to_rle:", rle_program.string_to_rle("10f:64"))
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 85]
    # print(bytes(l))
    # file = '880bbbbbb0bbbbbbbbbb0bb0bbbbbbbbbbbb0bb0bbbbb00bbbbbbbbbbb0bbbbbb0'
    # print(rle_program.to_rle_string(rle_program.encode_rle(file)))
    # file = console_gfx.load_file("testfiles/gator.gfx")
    # print("file: ",file)
    # print("encode ",rle_program.encode_rle(file))
    # print("testing:\n"+rle_program.to_rle_string(rle_program.encode_rle(file)))
    # print("2e:15d:15d:15d:13d:3a:6d:2a:2d:1a:1f:10:7a:12:15a:1d:9a:30:1a:1d:3a:60:3a:3d:8a:15d:15d:15d:15d:1d")
    # s = rle_program.to_hex_string([3, 'f', 6, 4])
    # print(s)
    # print(rle_program.count_runs([3,15,6,4]))
    # print(rle_program.to_hex_string([3, 15, 6, 4]))
    # print(rle_program.to_hex_string([15,15,15,4,4,4,4,4,4]))
    # print(int('B', 16))
    # print(int('b', 16))
    # print(rle_program.encode_rle("2e:15f:15f:5f:12:1a:12:6f:26:3f:12:2a:12:4f:46:3f:12:2a:22:2f:46:4f:12:2a:12:3f:26:2f:42:1a:12:1a:12:4f:22:1a:12:5a:12:3f:12:4a:12:4a:12:1f:22:10a:22:11a:12:1f:12:1a:32:2a:32:2a:12:1f:12:2a:12:1f:12:1a:12:2f:12:1a:12:2f:22:2f:12:2a:12:1f:12:2a:12"))
    file = "2e:15f:15f:5f:12:1a:12:6f:26:3f:12:2a:12:4f:46:3f:12:2a:22:2f:46:4f:12:2a:12:3f:26:2f:42:1a:12:1a:12:4f:22:1a:12:5a:12:3f:12:4a:12:4a:12:1f:22:10a:22:11a:12:1f:12:1a:32:2a:32:2a:12:1f:12:2a:12:1f:12:1a:12:2f:12:1a:12:2f:22:2f:12:2a:12:1f:12:2a:12"
    f = rle_program.string_to_rle(file)
    s = rle_program.encode_rle(f)
    x = rle_program.to_hex_string(s)
    v = rle_program.to_hex_string(f)
    print(f)
    print(s)
    print(x)
    print(v)
    for i in range(0,len(v),2):
        for j in range(0, int(v[i], 16)):
            print(v[i+1], end='')