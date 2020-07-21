from absl import app, logging, flags

FLAGS = flags.FLAGS
flags.DEFINE_string("name", None, "The program's name.")

def main(argv):

    if FLAGS.name is not None:
        print(FLAGS.name)

    return


if __name__ == "__main__":

    print(__name__)

    app.run(main)