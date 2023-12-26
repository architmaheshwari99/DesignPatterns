"""
with the Facade Pattern you can take a complex subsystem and make it easier to use
by implementing a Facade class that provides one, more reasonable interface
Facades don’t “encapsulate” the subsystem classes; they merely provide a simplified interface to their functionality. The subsystem classes still remain available
for direct use by clients that need to use more specific interfaces.

The Facade Pattern also allows you to decouple your client implementation from any one
subsystem.

The intent of the Adapter Pattern is to alter an interface so that it matches one a client is expecting.
The intent of the Facade Pattern is to provide a simplified interface to a subsystem.

the principle tells us that we should only invoke methods that belong to:(Principle of Least Knowledge)
- The object itself
- Objects passed in as a parameter to the method
- Any object the method creates or instantiates
- Any components of the object

"""

"""
class VideoFile
// ...

class OggCompressionCodec
// ...

class MPEG4CompressionCodec
// ...

class CodecFactory
// ...

class BitrateReader
// ...

class AudioMixer
// ...


// We create a facade class to hide the framework's complexity
// behind a simple interface. It's a trade-off between
// functionality and simplicity.
class VideoConverter is
    method convert(filename, format):File is
        file = new VideoFile(filename)
        sourceCodec = (new CodecFactory).extract(file)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Application classes don't depend on a billion classes
// provided by the complex framework. Also, if you decide to
// switch frameworks, you only need to rewrite the facade class.
class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()



"""
