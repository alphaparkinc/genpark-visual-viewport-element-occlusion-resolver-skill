from client import VisualViewportElementOcclusionResolverClient

def main():
    client = VisualViewportElementOcclusionResolverClient()
    res = client.resolve_occlusion_and_scroll('btn_submit')
    print('Viewport Occlusion Resolver: ' + res['occlusion_resolution_id'])
    print('Occluded: ' + str(res['is_occluded_by_overlay']) + ' (' + res['occluding_overlay_type'] + ')')
    print('Clickable: ' + str(res['element_now_clickable']) + ' | Grounding URL: ' + res['visual_grounding_url'])

if __name__ == '__main__':
    main()
