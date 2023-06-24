const uint8_t initial_bitmap[256][8] = {
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xc0, 0x00, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xc0, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xfe, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0x0f, 0xff, 0xfc, 0x07, 0xff, 0xff, 0xff, 0xff },
{ 0x09, 0xff, 0xfc, 0x03, 0xff, 0xff, 0xff, 0xff },
{ 0x00, 0xff, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff },
{ 0x00, 0x3f, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff },
{ 0x00, 0x07, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff },
{ 0x00, 0x01, 0xff, 0x01, 0xff, 0xff, 0xff, 0xff },
{ 0x00, 0x00, 0x7f, 0x01, 0x83, 0xff, 0xff, 0xff },
{ 0x00, 0x00, 0x7b, 0x00, 0x39, 0xff, 0xff, 0xff },
{ 0x00, 0x00, 0x3b, 0x80, 0x3c, 0x7f, 0xff, 0xff },
{ 0x00, 0x00, 0x3f, 0x00, 0x3c, 0x3f, 0xff, 0xff },
{ 0x00, 0x00, 0x19, 0x00, 0x3c, 0x1f, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x0e, 0x0f, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f, 0xff },
{ 0x00, 0x00, 0x09, 0x80, 0x00, 0x00, 0x7f, 0xff },
{ 0x00, 0x00, 0x19, 0xf8, 0x00, 0x00, 0x7f, 0xff },
{ 0x00, 0x00, 0x19, 0xfe, 0x0e, 0x00, 0x3f, 0xff },
{ 0x00, 0x00, 0x39, 0xfe, 0x05, 0xc0, 0x3f, 0xff },
{ 0x00, 0x00, 0x39, 0xfe, 0x00, 0x00, 0x3f, 0xff },
{ 0x00, 0x00, 0x39, 0xff, 0x00, 0x00, 0x3f, 0xff },
{ 0x00, 0x00, 0x39, 0xff, 0x00, 0x00, 0x3f, 0xff },
{ 0x00, 0x00, 0x38, 0x7f, 0x00, 0x00, 0x3f, 0xff },
{ 0x60, 0x08, 0x08, 0x3f, 0x00, 0x00, 0x0f, 0xff },
{ 0xff, 0xd8, 0x00, 0x07, 0x20, 0x00, 0x01, 0xff },
{ 0x7f, 0xf8, 0x00, 0x07, 0xe0, 0x00, 0x00, 0x7f },
{ 0x7f, 0xe0, 0x01, 0xff, 0xf0, 0x00, 0x00, 0x3f },
{ 0xff, 0xe0, 0x7f, 0xff, 0xf0, 0x00, 0x00, 0x0f },
{ 0xff, 0xc0, 0x7f, 0xff, 0xf1, 0xe0, 0x00, 0x03 },
{ 0xff, 0x80, 0x7f, 0xff, 0xf7, 0xff, 0x00, 0x01 },
{ 0xff, 0x80, 0x7f, 0xff, 0xf7, 0xff, 0xc0, 0x00 },
{ 0xff, 0x86, 0x7f, 0xff, 0xff, 0xff, 0xe0, 0x00 },
{ 0xff, 0x86, 0x7f, 0xff, 0xff, 0xff, 0xf8, 0x00 },
{ 0xff, 0x86, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xe0 },
{ 0xff, 0x86, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xe0 },
{ 0xff, 0x86, 0x67, 0xff, 0xff, 0xff, 0xff, 0xf0 },
{ 0xff, 0xc4, 0xcf, 0xff, 0xff, 0xff, 0xff, 0xfe },
{ 0xff, 0x84, 0x8f, 0xff, 0xff, 0xff, 0xff, 0xfe },
{ 0xff, 0x8c, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xfe },
{ 0xff, 0x8c, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x8c, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0xc8, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x80, 0xc1, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x80, 0xc7, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x80, 0x87, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x00, 0x87, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x92, 0x8f, 0xbf, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x92, 0x9f, 0xbf, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x02, 0x1f, 0xbf, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x02, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x02, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xff, 0x02, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x47, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x47, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x06, 0x47, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x04, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x00, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x00, 0x07, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x00, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfe, 0x00, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xf7 },
{ 0xfe, 0x00, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xf7 },
{ 0xff, 0x00, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xf3 },
{ 0xff, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xd3 },
{ 0xff, 0x00, 0xbf, 0xff, 0xff, 0xff, 0xff, 0xc3 },
{ 0xff, 0x00, 0x9f, 0xff, 0xff, 0xff, 0xff, 0xc3 },
{ 0xff, 0x00, 0xdf, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0x80, 0xcf, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0x80, 0xcf, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0x80, 0xef, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0x80, 0x6f, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0xc0, 0x7e, 0xff, 0xff, 0xff, 0xff, 0xe3 },
{ 0xff, 0x80, 0x7c, 0x7f, 0xff, 0xe7, 0xff, 0xe3 },
{ 0xff, 0xc0, 0x38, 0x7f, 0xff, 0xe3, 0xff, 0xe3 },
{ 0xff, 0xc0, 0x38, 0xf7, 0xff, 0xe3, 0xff, 0xe7 },
{ 0xff, 0xe0, 0x11, 0xcf, 0xff, 0xe1, 0xff, 0xc7 },
{ 0xff, 0xe0, 0x00, 0x1f, 0xff, 0xe1, 0xff, 0xc7 },
{ 0xff, 0xf0, 0x00, 0x3f, 0xff, 0xc1, 0xff, 0xc7 },
{ 0xff, 0xfc, 0x04, 0x7f, 0xff, 0xc1, 0xff, 0xc7 },
{ 0xff, 0xfe, 0x08, 0xff, 0xff, 0xc0, 0xff, 0xc7 },
{ 0xff, 0xff, 0x01, 0xff, 0xff, 0xc0, 0xdf, 0xc7 },
{ 0xff, 0xff, 0x87, 0xff, 0xff, 0xe0, 0xff, 0xc7 },
{ 0xff, 0xff, 0x8f, 0xff, 0xff, 0xe0, 0x7f, 0x87 },
{ 0xff, 0xff, 0x9f, 0xff, 0xff, 0xe0, 0x3f, 0x87 },
{ 0xff, 0xff, 0x9f, 0xff, 0xff, 0xf0, 0x3f, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf0, 0x1f, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf0, 0x1f, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x1f, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x0f, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x07, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x07, 0x87 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x03, 0xc7 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x07, 0xc7 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x07, 0xc7 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x0f, 0xc7 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x07, 0xc7 },
{ 0xff, 0xff, 0xbf, 0xff, 0xff, 0xf8, 0x03, 0xc7 },
{ 0xff, 0xff, 0x9f, 0xff, 0xff, 0xf8, 0x03, 0xc7 },
{ 0xff, 0xff, 0x8f, 0xff, 0xff, 0xf0, 0x03, 0xc7 },
{ 0xff, 0xfe, 0x07, 0xff, 0xff, 0xf0, 0x07, 0x87 },
{ 0xff, 0xfc, 0x01, 0xff, 0xff, 0xe0, 0x1f, 0x87 },
{ 0xff, 0xf8, 0x10, 0xff, 0xff, 0xe0, 0x1f, 0x8f },
{ 0xff, 0xf0, 0x0c, 0x7f, 0xff, 0xe0, 0x03, 0x8f },
{ 0xff, 0xe0, 0x0f, 0x7f, 0xff, 0xc0, 0x07, 0x8f },
{ 0xff, 0xc0, 0x7f, 0xbf, 0xff, 0xc0, 0x07, 0x8f },
{ 0xff, 0xc0, 0x7f, 0xdf, 0xff, 0xc0, 0x47, 0x8f },
{ 0xff, 0x80, 0x3f, 0xff, 0xff, 0xc0, 0xcf, 0x8f },
{ 0xff, 0x80, 0x7f, 0xef, 0xff, 0xc0, 0xe3, 0x8f },
{ 0xff, 0x00, 0x7f, 0xf7, 0xff, 0xc1, 0xf3, 0x8f },
{ 0xfe, 0x00, 0xff, 0xff, 0xff, 0xc1, 0xf1, 0x8f },
{ 0xfe, 0x00, 0xff, 0xff, 0xff, 0xc1, 0xef, 0x87 },
{ 0xfe, 0x00, 0xdf, 0xff, 0xff, 0xc3, 0xcb, 0xc7 },
{ 0xfe, 0x00, 0xbf, 0xff, 0xff, 0xc3, 0xf9, 0xc7 },
{ 0xfe, 0x01, 0xbf, 0xff, 0xff, 0x87, 0xed, 0xc7 },
{ 0xfc, 0x01, 0x3f, 0xff, 0xff, 0x87, 0xff, 0xc7 },
{ 0xfe, 0x01, 0x7f, 0xff, 0xff, 0xff, 0xfb, 0xc7 },
{ 0xfe, 0x03, 0x7f, 0xff, 0xff, 0xff, 0xf3, 0xc7 },
{ 0xfc, 0x02, 0x7f, 0xff, 0xff, 0xff, 0xfe, 0xc7 },
{ 0xf8, 0x02, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x47 },
{ 0xf8, 0x00, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x47 },
{ 0xf8, 0x04, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc7 },
{ 0xf8, 0x00, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xc7 },
{ 0xf8, 0x04, 0x3f, 0xff, 0xff, 0xff, 0xff, 0x07 },
{ 0xf8, 0x0c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0x07 },
{ 0xf0, 0x0c, 0x1f, 0xff, 0xff, 0xff, 0xfe, 0x0f },
{ 0xf0, 0x0c, 0x1f, 0xff, 0xff, 0xff, 0xfe, 0x0f },
{ 0xf0, 0x0d, 0x1f, 0xff, 0xff, 0xff, 0xfe, 0x0f },
{ 0xf0, 0x09, 0x1f, 0xff, 0xff, 0xff, 0xfe, 0x0f },
{ 0xf0, 0x09, 0x1f, 0xff, 0xff, 0xff, 0xf8, 0x0f },
{ 0xf8, 0x4c, 0x1f, 0xff, 0xff, 0xff, 0xfc, 0x0f },
{ 0xf8, 0x4c, 0x1e, 0xff, 0xff, 0xff, 0xff, 0x0f },
{ 0xf8, 0x4c, 0x1e, 0xff, 0xff, 0xff, 0xff, 0x0f },
{ 0xf8, 0xcc, 0x1e, 0xff, 0xff, 0xff, 0xff, 0xef },
{ 0xf8, 0xcc, 0x3e, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xf8, 0xc4, 0x3e, 0xff, 0xff, 0xff, 0xff, 0x9f },
{ 0xfc, 0xc4, 0x7e, 0xff, 0xff, 0xff, 0xff, 0x8f },
{ 0xfc, 0xd4, 0x7e, 0xff, 0xff, 0xff, 0xff, 0x9f },
{ 0xfc, 0xd6, 0x3c, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xd2, 0x3c, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xda, 0x1d, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xda, 0x3d, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xda, 0x39, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xd8, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff },
{ 0xfc, 0xd8, 0x03, 0xff, 0xff, 0xff, 0xff, 0xfe },
{ 0xfc, 0xdc, 0x07, 0xff, 0xff, 0xff, 0xff, 0xfe },
{ 0xfc, 0x5c, 0x0f, 0xff, 0xff, 0xff, 0xff, 0xfc },
{ 0xfc, 0x5c, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xfc },
{ 0xfc, 0x1e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xfc },
{ 0xfc, 0x1f, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xfc },
{ 0xfc, 0x1f, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xf8 },
{ 0xfc, 0x1f, 0x9f, 0xff, 0xff, 0xff, 0xff, 0xf8 },
{ 0xfc, 0x1f, 0xbf, 0xff, 0xff, 0xff, 0xff, 0xe0 },
{ 0xfc, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0x40 },
{ 0xfc, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00 },
{ 0xfe, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00 },
{ 0xfe, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x00 },
{ 0x7e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x00 },
{ 0x1e, 0x03, 0xff, 0xff, 0xff, 0xff, 0xa0, 0x00 },
{ 0x17, 0x00, 0x3f, 0xff, 0xff, 0xfc, 0x80, 0x00 },
{ 0x00, 0xc0, 0x0f, 0xff, 0xff, 0xf0, 0x00, 0x00 },
{ 0x00, 0x00, 0x03, 0xff, 0xff, 0x80, 0x00, 0x00 },
{ 0x00, 0x00, 0x61, 0xff, 0xff, 0x80, 0x00, 0x00 },
{ 0x00, 0x00, 0x6f, 0xff, 0xff, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x4f, 0xff, 0xfe, 0x00, 0x00, 0x03 },
{ 0x00, 0x00, 0x5f, 0xff, 0xfc, 0x00, 0x00, 0x07 },
{ 0x00, 0x00, 0x1f, 0xff, 0xf8, 0x00, 0x00, 0x1f },
{ 0x00, 0x00, 0x01, 0xff, 0xe0, 0x00, 0x00, 0x7f },
{ 0x00, 0x00, 0x00, 0xff, 0xf8, 0x00, 0x01, 0xff },
{ 0x00, 0x00, 0x01, 0xff, 0xfe, 0x00, 0x1f, 0xff },
{ 0x00, 0x00, 0x03, 0xff, 0xff, 0xe5, 0xff, 0xff },
{ 0x00, 0x00, 0x01, 0xff, 0xff, 0xc7, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0xff, 0xfe, 0x03, 0xff, 0xff },
{ 0x00, 0x0e, 0x00, 0x03, 0xf0, 0x03, 0xff, 0xff },
{ 0x00, 0x06, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff },
{ 0x00, 0x02, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff },
{ 0x00, 0x02, 0x00, 0x00, 0x00, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x01, 0x44, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x01, 0xc4, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x01, 0xc8, 0x03, 0xff, 0xff },
{ 0x00, 0x00, 0x00, 0x01, 0xf8, 0x07, 0xff, 0xff },
{ 0x00, 0x00, 0x01, 0x81, 0xfb, 0x07, 0xff, 0xff },
{ 0x00, 0x00, 0x01, 0xc1, 0xd3, 0x07, 0xff, 0xff },
{ 0x00, 0x00, 0x81, 0xc1, 0xc3, 0x0f, 0xff, 0xff },
{ 0xc0, 0x0e, 0x01, 0xe3, 0xe2, 0x0f, 0xff, 0xff },
{ 0xe0, 0x3f, 0x01, 0xff, 0xe0, 0x1f, 0xff, 0xff },
{ 0xff, 0xff, 0x00, 0xff, 0xc6, 0x3f, 0xff, 0xff },
{ 0xff, 0xff, 0x00, 0x7f, 0xc6, 0x7f, 0xff, 0xff },
{ 0xff, 0xff, 0x01, 0xff, 0x8e, 0xff, 0xff, 0xff },
{ 0xff, 0xff, 0x01, 0xff, 0x1d, 0xff, 0xff, 0xff },
{ 0xff, 0xff, 0x81, 0xfe, 0x1f, 0xff, 0xff, 0xff },
{ 0xff, 0xff, 0xe3, 0xff, 0xbf, 0xff, 0xff, 0xff },
{ 0xff, 0xff, 0xf3, 0xff, 0xff, 0xff, 0xff, 0xfc },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x00, 0x00 },
{ 0xff, 0xff, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00 },
{ 0x3f, 0xff, 0xff, 0xe0, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x03, 0xe8, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
{ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 },
};