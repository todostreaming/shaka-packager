# Copyright 2014 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'includes': [
    '../../../common.gypi',
  ],
  'targets': [
    {
      'target_name': 'mp2t',
      'type': '<(component)',
      'sources': [
        'adts_header.cc',
        'adts_header.h',
        'continuity_counter.cc',
        'continuity_counter.h',
        'es_parser_adts.cc',
        'es_parser_adts.h',
        'es_parser_h264.cc',
        'es_parser_h264.h',
        'es_parser_h265.cc',
        'es_parser_h265.h',
        'es_parser_h26x.cc',
        'es_parser_h26x.h',
        'es_parser.h',
        'mp2t_media_parser.cc',
        'mp2t_media_parser.h',
        'pes_packet.cc',
        'pes_packet.h',
        'pes_packet_generator.cc',
        'pes_packet_generator.h',
        'program_map_table_writer.cc',
        'program_map_table_writer.h',
        'ts_muxer.cc',
        'ts_muxer.h',
        'ts_packet.cc',
        'ts_packet.h',
        'ts_packet_writer_util.cc',
        'ts_packet_writer_util.h',
        'ts_section_pat.cc',
        'ts_section_pat.h',
        'ts_section_pes.cc',
        'ts_section_pes.h',
        'ts_section_pmt.cc',
        'ts_section_pmt.h',
        'ts_section_psi.cc',
        'ts_section_psi.h',
        'ts_segmenter.cc',
        'ts_segmenter.h',
        'ts_writer.cc',
        'ts_writer.h',
      ],
      'dependencies': [
        '../../base/media_base.gyp:media_base',
        '../../codecs/codecs.gyp:codecs',
      ],
    },
    {
      'target_name': 'mp2t_unittest',
      'type': '<(gtest_target_type)',
      'sources': [
        'adts_header_unittest.cc',
        'es_parser_h264_unittest.cc',
        'es_parser_h26x_unittest.cc',
        'mp2t_media_parser_unittest.cc',
        'pes_packet_generator_unittest.cc',
        'program_map_table_writer_unittest.cc',
        'ts_segmenter_unittest.cc',
        'ts_writer_unittest.cc',
      ],
      'dependencies': [
        '../../../testing/gtest.gyp:gtest',
        '../../../testing/gmock.gyp:gmock',
        '../../codecs/codecs.gyp:codecs',
        '../../event/media_event.gyp:mock_muxer_listener',
        '../../test/media_test.gyp:media_test_support',
        '../mpeg/mpeg.gyp:mpeg',
        'mp2t',
      ]
    },
  ],
}
