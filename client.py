class VisualViewportElementOcclusionResolverClient:
    def resolve_occlusion_and_scroll(self, target_element_id='btn_checkout', viewport_bounds={'width': 1920, 'height': 1080}):
        return {
            'occlusion_resolution_id': 'occ_res_8812',
            'target_element_id': target_element_id,
            'is_occluded_by_overlay': True,
            'occluding_overlay_type': 'COOKIE_CONSENT_MODAL',
            'dismissal_action_executed': 'DISMISS_COOKIE_BANNER_PRE_ACTION',
            'optimal_scroll_offset_y': 340,
            'element_now_clickable': True,
            'visual_grounding_url': 'https://computeruse.grounding.genpark.ai/occlusions/8812.json'
        }
