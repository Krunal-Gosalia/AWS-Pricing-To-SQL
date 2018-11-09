USE [dbname]
GO

/****** Object:  Table [dbo].[AmazonS3]    Script Date: 10/23/2018 3:05:03 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[AmazonS3](
	[SKU] [nvarchar](255) NULL,
	[OfferTermCode] [nvarchar](255) NULL,
	[RateCode] [nvarchar](255) NULL,
	[TermType] [nvarchar](255) NULL,
	[PriceDescription] [nvarchar](255) NULL,
	[EffectiveDate] [datetime] NULL,
	[StartingRange] [float] NULL,
	[EndingRange] [nvarchar](255) NULL,
	[Unit] [nvarchar](255) NULL,
	[PricePerUnit] [float] NULL,
	[Currency] [nvarchar](255) NULL,
	[Product Family] [nvarchar](255) NULL,
	[serviceCode] [nvarchar](255) NULL,
	[Location] [nvarchar](255) NULL,
	[Location Type] [nvarchar](255) NULL,
	[Availability] [float] NULL,
	[Storage Class] [nvarchar](255) NULL,
	[Volume Type] [nvarchar](255) NULL,
	[Fee Code] [nvarchar](255) NULL,
	[Fee Description] [nvarchar](255) NULL,
	[Group] [nvarchar](255) NULL,
	[Group Description] [nvarchar](255) NULL,
	[Transfer Type] [nvarchar](255) NULL,
	[From Location] [nvarchar](255) NULL,
	[From Location Type] [nvarchar](255) NULL,
	[To Location] [nvarchar](255) NULL,
	[To Location Type] [nvarchar](255) NULL,
	[usageType] [nvarchar](255) NULL,
	[operation] [nvarchar](255) NULL,
	[Durability] [float] NULL,
	[serviceName] [nvarchar](255) NULL
) ON [PRIMARY]
GO

