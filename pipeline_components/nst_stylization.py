import os
import subprocess


# todo: consider optimizing - batch of images to be styled
def stylization(frames_path, model_name, img_width):
    stylized_frames_dump_dir = os.path.join(frames_path, os.path.pardir, os.path.pardir, model_name.split('.')[0], 'stylized')
    os.makedirs(stylized_frames_dump_dir, exist_ok=True)

    if len(os.listdir(stylized_frames_dump_dir)) == 0:
        print('*' * 20, 'Frame stylization stage started', '*' * 20)
        for frame_name in os.listdir(frames_path):
            frame_path = os.path.join(frames_path, frame_name)
            stylization_script_path = os.path.join(os.path.dirname(__file__), os.path.pardir, 'pytorch-nst-feedforward', 'stylization_script.py')
            subprocess.call(['python', stylization_script_path, '--content_img_name', frame_path, '--img_width', str(img_width), '--model_name', model_name, '--should_not_display', '--redirected_output', stylized_frames_dump_dir])
            print(f'Stylizing frame {frame_name} - batch size 1')
    else:
        print('Skipping frame stylization, already done.')

    return {"stylized_frames_path": stylized_frames_dump_dir}